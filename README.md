Plover auto reconnect writer
============================

An extension to [Plover](https://github.com/openstenoproject/plover) to automatically reconnect a steno machine if it got disconnected.

How to Use
----------

This plugin enhances plover by automatically reconnecting the steno machine to plover.
Without the machine it is necessary to hit the reconnect button in plover in some cases.
As soon as the steno machine is connected, the plugin will trigger a reconnect in plover.

Using the plugin, it doesn't matter any more, if you start plover before connecting the steno machine or the other way round.

The plugin does also allow to unplug and replug the steno machine or to switch devices (unplug machine A, plug in machine B) -- as long as they will use the same com port and protocol.

What this plugin does not
-------------------------

This plugin intentionally does not do any kind of auto discover.
You need to have your machine correctly configured for this plugin to work.

Installation
------------

Download the latest version of Plover for your operating system from the [releases page](https://github.com/openstenoproject/plover/releases). Only versions 4.0.0rc2 and higher are supported.

To install the cloned git repository, you can run the following command:

Windows

.. code:: powershell

	.\plover_console.exe -s plover_plugins install <path-to-plover-auto-reconnect-machine-git-repo>

Mac

.. code:: bash

	/Applications/Plover.app/Contents/MacOS/Plover -s plover_plugins install <path-to-plover-auto-reconnect-machine-git-repo>

Or you can install the latest released version using the Plugin Manager

1. Open Plover
2. Navigate to the Plugin Manager tool
3. Select the "plover-auto-reconnect-machine" plugin entry in the list
4. Click install
5. Restart Plover
6. Activate the plugin in the plugin tab of the plover configuration dialog

The same method can be used for updating and uninstalling the plugin.
