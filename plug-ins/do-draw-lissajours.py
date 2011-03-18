#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import itertools, math

def do_draw_lissajours(A, B, a, b, delta, tmin, tmax):
    # 画像の幅、高さ、中心座標を計算する
    w, h, cx, cy = A*4, B*4, A*2, B*2
    
    # 画像とその上におくレイヤーを作成する
    img = gimp.Image(w, h)
    lay = gimp.Layer(img, 'lissajours', w, h)
    img.add_layer(lay)
    
    # レイヤーの上のイメージを初期化して、色を設定する
    pdb.gimp_edit_clear(lay)
    pdb.gimp_context_set_foreground((0,0,0))
    
    # t を tmin から tmax まで変化させたときの
    # 座標からなるタプルを作る
    trange = range(tmin, tmax)
    points = tuple(itertools.chain(
        *((A*math.cos(a*t)+cx, B*math.sin(b*t+delta)+cy)
        for t in trange)))

    # 座標値の列を使って曲線を描く
    pdb.gimp_paintbrush_default(lay, len(points), points)
    
    # 描画結果を表示する
    d = gimp.Display(img)


register(
    "Lissajours",   # プロシジャの名前
    "Draws Lissajours' curve.\n" \ # プロシジャの説明
    "x=Acos(at), y=Bsin(bt+delta), [tmin<t<tmax]",
    "Draws Lissajours' curve", # PDBに登録する追加情報 
    "Yasushi Masuda", # プロシジャの作者
    "Placed on Public Domain.", # ライセンス情報
    "2008", # 作成日
    "Lissajours", # メニューに表示する名前
    "", # 対応する画像タイプ
    [(PF_FLOAT, "A", "Parameter A", 200),
    (PF_FLOAT, "B", "Parameter B", 200),
    (PF_FLOAT, "a", "Parameter a", 0.03),
    (PF_FLOAT, "b", "Parameter b", 0.09),
    (PF_FLOAT, "delta", "Parameter delta", 200),
    (PF_INT, "tmin", "Parameter tmin", 0),
    (PF_INT, "tmax", "Parameter tmax", 1000)], # 引数定義
    [], # 戻り値定義
    do_draw_lissajours, # 処理する関数名
    menu="<Toolbox>/Xtns/MySample", # メニューを表示させる場所
)

main()
