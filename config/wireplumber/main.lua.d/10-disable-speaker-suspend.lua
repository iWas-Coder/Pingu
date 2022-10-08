local rule = {
    matches = {
        {
            { "node.name", "equals", "alsa_output.usb-Focusrite_Scarlett_Solo_USB_Y76639U042FF12-00.analog-stereo" },
            { "node.name", "equals", "alsa_output.pci-0000_0a_00.1.hdmi-stereo" },
        }
    },
    apply_properties = {
        ["session.suspend-timeout-seconds"] = 0
    }
}

table.insert(alsa_monitor.rules, rule)
