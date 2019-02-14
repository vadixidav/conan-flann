from conans import ConanFile, CMake, tools


class FlannConan(ConanFile):
    name = "flann"
    version = "1.9.1"
    license = "BSD"
    url = "https://github.com/mariusmuja/flann"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        tools.get(
            "https://github.com/mariusmuja/flann/archive/{}.zip".format(self.version), destination=".")

    def build(self):
        cmake = CMake(self)
        cmake.configure(
            source_folder="{}/{}-{}".format(self.source_folder, self.name, self.version))
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
