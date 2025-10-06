import platform
import sys
import os

def get_os_info():
    system = platform.system().lower()
    release = platform.release()
    version = platform.version()

    if system == "windows":
        return {"os": "windows", "release ": release, "version ": version}
    elif system == "linux":
        try:
            import distro
            distro_name = distro.name(pretty=True)
            return {"os": "linux", "Distro ": distro_name, "release ": release}
        except ImportError:
            return {"os": "linux", "release ": release}
    
    elif system == "darwin":
        return {"os": "macOS", "release ": release, "version ": version}
    else:
        return {"os": "Unknown", "release ": release, "version ": version}


def is_supported():
    """Check if current OS is supported by the assistant bot."""
    supported_systems = ["windows", "linux", "darwin"]
    return platform.system().lower() in supported_systems


if __name__ == "__main__":
    info = get_os_info()
    print("Detected OS Info:", info)
    print("Supported:", is_supported())