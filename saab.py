import winreg

reg_key_CLSID_name = r"Software\Microsoft\Windows\CurrentVersion\Explorer\CLSID"


def main():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key_CLSID_name) as key:
        subkey_count, value_count, _ = winreg.QueryInfoKey(key)
        print(f"{reg_key_CLSID_name}\n{subkey_count=}, {value_count=}")

        subkey_name_xs = [winreg.EnumKey(key, i) for i in range(subkey_count)]

        for i, k in enumerate(subkey_name_xs):
            print(i + 1, end=" ")
            list_empty_subkeys(key, k)


def list_empty_subkeys(root_key, sub_key):
    try:
        with winreg.OpenKey(root_key, sub_key, 0, winreg.KEY_READ) as key:
            subkey_count, value_count, _ = winreg.QueryInfoKey(key)
            if subkey_count == 0 and value_count == 0:
                print(f"Empty subkey: {sub_key}", end=" ")
                winreg.DeleteKey(root_key, sub_key)
                print("deleted !!! ")
            else:
                print(f"         key: {sub_key}")

    except FileNotFoundError:
        print(f"Key not found: {sub_key}")
    except PermissionError:
        print(f"Permission denied: {sub_key}")


if __name__ == "__main__":
    main()
