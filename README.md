This repository contains a tool for static analysis of OpenBSD's kernel locking.
The work was sponsored by [genua GmbH](https://www.genua.de/).

# Lock Balancing Checker

Checks the
[spl(9)](https://man.openbsd.org/spl.9)
locking semantics of OpenBSD kernel source code.
This is performed by analyzing each function of a file.
It counts all calls to lock/unlock functions.
At the end of each function,
the number of calls to all locking operations need to be equal to
the number of calls to all unlocking operations.
They need to be balanced.

## Preparation

This script and all actions described here need to be run on an OpenBSD system
with all sets installed.
Make sure your user is in the `wsrc` and `wobj` groups.

Install python3

```
doas pkg_add python3
```

Create a Python virtual environment,
which will be used for all additional packages.

```
python3 -m venv /tmp/py
. /tmp/py/bin/activate
```

Clone this repository.
Install the Lock Balancing Checker script (lbc).

```
python3 ./setup.py install
```

Apply the [patch](./config.patch) to the OpenBSD source tree.
The patch teaches config(8) to emit preprocessed source files and adds necessary
rules to the AMD64 kernel build to use them.
Then rebuild and install config(8).

```
cd /usr/src/usr.sbin/config
make obj && make
doas make install
```

After that, prepare the kernel object directory.
You do not need to build or install it for the analysis.

```
cd /sys/arch/$(machine)/compile/GENERIC.MP
make obj
make config
```

## Analysis

To run `lbc`, go to the kernel build directory and invoke the following command.

```
cd /sys/arch/$(machine)/compile/GENERIC.MP/obj
make lbc
```

All results need to be validated!

## TODO

* Handling goto labels is inconsistent.
  Especially for code that jumps into loops,
  or switch cases.
* Convert to a proper Python module
* Add tests
