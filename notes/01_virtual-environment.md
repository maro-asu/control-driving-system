Python仮想環境について

python3 -m venv .venv　//仮想環境を作成

source .venv/bin/activate　//仮想環境を有効化

python -m pip install numpy matplotlib japanize-matplotlib //モジュールインストール

deactivate　//仮想環境を終了


1.Ctrl+Shift+P でコマンドパレットを開く．
2.Python: Select Interpreter を選ぶ．
3..venv 内のPythonを選ぶ．

一度選ぶとそのリポジトリで選択が記憶される．
以降は，VSCodeで新しいターミナルを開くと自動で activate された状態になる．