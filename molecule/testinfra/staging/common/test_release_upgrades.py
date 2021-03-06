def test_release_manager_upgrade_channel(host):
    """
    Ensures that the `do-release-upgrade` command will honor
    upgrades from Trusty to Xenial, but not suggest upgrades
    from Xenial to Bionic (which is untested and unsupported.)
    """
    expected_channels = {
        "trusty": "lts",
        "xenial": "never",
    }

    config_path = "/etc/update-manager/release-upgrades"
    assert host.file(config_path).is_file

    raw_output = host.check_output("grep '^Prompt' {}".format(config_path))
    _, channel = raw_output.split("=")

    expected_channel = expected_channels[host.system_info.codename]
    assert channel == expected_channel


def test_do_release_upgrade_is_installed(host):
    """
    Ensure the `do-release-upgrade` command is present on target systems,
    so that instance Admins can upgrade from Trusty to Xenial.
    """
    assert host.exists("do-release-upgrade")
