import os
import importlib
import json
import sys
from pathlib import Path

# バナー表示
def show_banner():
    with open("banner.txt", "r", encoding="utf-8") as f:
        print(f.read())

# 設定ファイル読み込み
def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

# プラグイン読み込み
def load_plugins():
    plugins = {}
    plugin_dir = Path("plugins")
    for plugin_file in plugin_dir.glob("*.py"):
        module_name = f"plugins.{plugin_file.stem}"
        module = importlib.import_module(module_name)
        if hasattr(module, "run"):
            plugins[module_file.stem] = module
    return plugins

# メインループ
def main():
    show_banner()
    config = load_config()
    plugins = load_plugins()

    print("多機能クライアント型サーバー 起動中...")
    print("使用可能なプラグイン:", ", ".join(plugins.keys()))
    
    while True:
        try:
            command = input("> ").strip()
            if command == "exit":
                print("サーバーを終了します。")
                break
            elif command in plugins:
                plugins[command].run()
            else:
                print("不明なコマンドです。")
        except KeyboardInterrupt:
            print("\nサーバーを終了します。")
            break

if __name__ == "__main__":
    main()