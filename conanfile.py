from tempfile import mkdtemp
from os import path
from conans import ConanFile, AutoToolsBuildEnvironment, tools


class FlexConan(ConanFile):
    name = "flex"
    version = "2.6.4"
    license = "https://github.com/westes/flex/blob/master/COPYING"
    url = "https://github.com/uilianries/conan-flex"
    author = "Uilian Ries <uilianries@gmail.com>"
    descriptions = "Flex, the fast lexical analyzer generator."
    settings = "os", "compiler", "build_type", "arch"
    generators = "txt", "cmake"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    release_name = "%s-%s" % (name, version)
    install_dir = mkdtemp(prefix=name)
    exports = "LICENSE"

    def source(self):
        tools.get("https://github.com/westes/flex/releases/download/v2.6.4/flex-%s.tar.gz" % self.version)

    def configure(self):
        if self.settings.os == "Windows":
            raise Exception("Flex is not supported on Windows.")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        with tools.environment_append(env_build.vars):
            configure_args = ['--prefix=%s' % self.install_dir]
            with tools.chdir(self.release_name):
                env_build.configure(args=configure_args)
                env_build.make(args=["all"])
                env_build.make(args=["install"])

    def package(self):
        self.copy(pattern="COPYING", dst=".", src=self.release_name)
        self.copy(pattern="*.h", dst="include", src=path.join(self.install_dir, "include"))
        self.copy(pattern="*", dst="bin", src=path.join(self.install_dir, "bin"))
        if self.options.shared:
            self.copy(pattern="*.so*", dst="lib", src=path.join(self.install_dir, "lib"))
        else:
            self.copy(pattern="*.a", dst="lib", src=path.join(self.install_dir, "lib"))
            self.copy(pattern="*.la", dst="lib", src=path.join(self.install_dir, "lib"))

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()
