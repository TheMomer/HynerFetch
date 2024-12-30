import os
import sys
import shutil
import platform
import subprocess

def is_admin():
    """Проверка прав администратора"""
    try:
        if platform.system() == 'Windows':
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin()
        else:
            return os.geteuid() == 0
    except:
        return False

def install_requirements():
    """Установка зависимостей из requirements.txt"""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt', '--break-system-packages'])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке зависимостей: {e}")
        return False

def install_windows():
    """Установка HyperFetch на Windows"""
    try:
        # Создаем директорию .hyperfetch в домашней папке пользователя
        home_dir = os.path.expanduser('~')
        hyperfetch_dir = os.path.join(home_dir, '.hyperfetch')
        
        # Копируем .hyperfetch
        if os.path.exists(hyperfetch_dir):
            shutil.rmtree(hyperfetch_dir)
        shutil.copytree('.hyperfetch', hyperfetch_dir)
        
        # Копируем исполняемый файл в System32
        system32_path = os.path.join(os.environ['WINDIR'], 'System32')
        shutil.copy2('hyperfetch', os.path.join(system32_path, 'hyperfetch.exe'))
        
        print("HyperFetch успешно установлен!")
        return True
    except Exception as e:
        print(f"Ошибка при установке: {e}")
        return False

def install_unix():
    """Установка HyperFetch на Unix-подобные системы"""
    try:
        # Создаем директорию .hyperfetch в домашней папке пользователя
        home_dir = os.path.expanduser('~')
        hyperfetch_dir = os.path.join(home_dir, '.hyperfetch')
        
        # Копируем .hyperfetch
        if os.path.exists(hyperfetch_dir):
            shutil.rmtree(hyperfetch_dir)
        shutil.copytree('.hyperfetch', hyperfetch_dir)
        
        # Копируем исполняемый файл в /usr/bin
        shutil.copy2('hyperfetch', '/usr/bin/hyperfetch')
        os.chmod('/usr/bin/hyperfetch', 0o755)
        
        print("HyperFetch успешно установлен!")
        return True
    except Exception as e:
        print(f"Ошибка при установке: {e}")
        return False

def main():
    """Основная функция установки"""
    if not is_admin():
        print("Для установки требуются права администратора!")
        print("Пожалуйста, запустите установщик с правами администратора.")
        sys.exit(1)

    print("Установка зависимостей...")
    if not install_requirements():
        print("Ошибка при установке зависимостей!")
        sys.exit(1)

    print("Установка HyperFetch...")
    if platform.system() == 'Windows':
        if not install_windows():
            print("Ошибка при установке HyperFetch!")
            sys.exit(1)
    else:
        if not install_unix():
            print("Ошибка при установке HyperFetch!")
            sys.exit(1)

    print("\nУстановка завершена!")
    print("Вы можете запустить HyperFetch командой 'hyperfetch'")

if __name__ == "__main__":
    main()