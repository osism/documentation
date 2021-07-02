# OSISM documentation

Published at https://docs.osism.tech.

## Install dependencies for building documentation

https://docs.openstack.org/doc-contrib-guide/docs-builds.html#install-dependencies-for-building-documentation

* On Ubuntu or Debian:

  ```
  # apt-get install python3-pip
  # pip3 install tox
  ```

* On RHEL or CentOS (replace yum with dnf on Fedora):

  ```
  # yum install python3-pip
  # pip3 install tox
  ```

* On openSUSE or SUSE Linux Enterprise:

  ```
  # zypper in python3-pip
  # pip3 install tox
  ```

* On MacOS:

  ```
  $ brew install python3
  $ pip3 install tox
  ```

* On Windows:

  ```
  $ pip3 install tox
  ```

## Building

All guides are in the RST format. You can use tox to prepare virtual environment and build all
guides (HTML only):

```
$ tox -e build
```

You can find the root of the generated HTML documentation at `build/html`.

## Pushing

```
$ export FTP_USERNAME=username
$ export FTP_PASSWORD=password
$ tox -e push
```

## Generated files

Some documentation files are generated using tools. These files include a `do not edit`
header and should not be modified by hand.

## License

This documentation was created by [OSISM GmbH](https://osism.tech)
and is licensed under a [Creative Commons Attribution 4.0 International Licence (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/).

[![Creative Commons Attribution-ShareAlike 4.0 International](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)
