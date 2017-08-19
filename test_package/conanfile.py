import os
from subprocess import check_call
from conans import ConanFile, CMake, tools


class FlexTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    user = os.getenv("CONAN_USERNAME", "conan")
    channel = os.getenv("CONAN_CHANNEL", "testing")
    generators = "cmake"
    requires = "flex/2.6.4@%s/%s" % (user, channel)
    
    def imports(self):
        self.copy(pattern="*", dst="bin", src="bin")

    def test(self):
        with tools.chdir("bin"):
            assert(os.path.isfile("flex"))
            check_call(["./flex", "--version"])
