from plover import log
from plover.engine import StenoEngine
from plover.machine.base import STATE_ERROR, SerialStenotypeBase

from serial.tools import list_ports

from time import sleep

from threading import Condition, Event, Thread



class AutoReconnectMachine:
    """Listen to the machine state and try to automatically
       reconnect as soon as the connection is available again."""

    def __init__(self, engine: StenoEngine):
        super().__init__()
        log.info('plover-auto-reconnect-machine: initializing')
        self._engine: StenoEngine = engine
        self._lock = Condition()
        self._stop = Event()
        self._thread = Thread(target=self.run)

    def start(self):
        log.info('plover-auto-reconnect-machine: starting')
        self._engine.hook_connect("machine_state_changed", self._on_machine_state_changed)
        self._thread.start()

    def stop(self):
        log.info('plover-auto-reconnect-machine: stopping')
        self._stop.set()
        self._notify()
        self._engine.hook_disconnect("machine_state_changed", self._on_machine_state_changed)

    def run(self):
        while not self._stop.isSet():
            if self._engine.machine_state != STATE_ERROR:
                log.info('plover-auto-reconnect-machine: machine is connected')
                # wait until notified
                self._wait()
            if self._engine.machine_state == STATE_ERROR:
                if isinstance(self._engine._machine, SerialStenotypeBase) and not self._port_exists(self._engine._machine.serial_params['port']):
                    log.info('plover-auto-reconnect-machine: machine can not be reconnected, retrying later')
                else:
                    log.info('plover-auto-reconnect-machine: machine is disconnected, trying to reconnect')
                    self._engine.reset_machine()

                # prevent busy endless loop, just check again in one second
                sleep(1)

    def _on_machine_state_changed(self, machine_type: str, machine_state: str):
        if machine_state == STATE_ERROR:
            self._notify()

    def _wait(self):
        with self._lock:
            self._lock.wait()

    def _notify(self):
        with self._lock:
            self._lock.notify()

    def _port_exists(self, portName):
        for port in list_ports.comports():
            if port.device == portName:
                return True
        return False
