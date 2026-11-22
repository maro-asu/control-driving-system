MatplotlibのGUI表示環境について

plt.show()を実行してもグラフが表示されなかった．

Matplotlibは，計算結果をグラフにするだけでなく，そのグラフを画面に表示する機能も持っている．

ただし，グラフの表示方法には複数の種類がある．

例えば，
- TkAgg
- QtAgg
- Agg
など．

このうち，今回使われていたのは Agg というバックエンドだった．

Aggは，グラフを画像として描画するための仕組みであるため，例えば，グラフをPNG画像として保存することはできる．
しかし，通常のGUIウィンドウを開いてグラフを表示する機能は持っていない．そのため，グラフ表示ができなかった．

WindowsでPythonを実行した場合，WindowsのGUI環境を利用してグラフを表示できる．
一方，WSLはWindows上でLinuxを動かす仕組みであるため，Linux側のPythonからGUIアプリケーションを表示するには，Windows側に画面を表示するための仕組みが必要になる．

現在のWSLには，WSLgというGUIアプリケーションを表示する仕組みが用意されている．
しかし，バックエンドがaggなので，GUI表示に対応したバックエンドを使うため，Tkinterを利用した．

Tkinterとは，PythonからGUIウィンドウを扱うための標準ライブラリである．

matplotlib.use('TkAgg')によって，「Matplotlibに対してTkinterを使ったGUI表示方式を利用する」と指定している．

利用してみて，個人的にはPythonのTkinterとJavaのswingは機能が似ているライブラリだと感じた．
どちらもGUIアプリをつくるためのライブラリとして存在する．

swingで
JButton button = new JButton("開始");
panel.add(button);
と書いていたものは，

Tkinterでは
button = tk.Button(panel, text="開始")
button.pack()
と書くことができる．

どちらも
1. GUI部品を作る
2. 部品をパネルなどに配置する
3. ボタンを押したときの処理を設定する
という流れになっている．

TkinterもSwingも，GUI部品を組み合わせて画面を構成する仕組みであるとわかる．
