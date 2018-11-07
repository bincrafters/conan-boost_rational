#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostRationalConan(base.BoostBaseConan):
    name = "boost_rational"
    url = "https://github.com/bincrafters/conan-boost_rational"
    lib_short_names = ["rational"]
    header_only_libs = ["rational"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_utility"
    ]


