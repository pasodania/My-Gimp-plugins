#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import os, glob

def do_scale_batch(dirname, ext, suffix, scale):
    # 指定のフォルダの有無を調べて、ファイルのリストを作成する
    if os.path.exists(dirname):
        fnames = [f for f in glob.glob(os.path.join(dirname, '*'+ext))
                    if suffix not in f]

        for fname in fnames:
            # ファイルを一つずつ開いてサイズを買え、suffix付きの名前で保存する
            new_filename = fname[:0-len(ext)]+suffix+ext
            img = pdb.gimp_file_load(fname, '')
            img.scale(int(img.width*scale), int(img.height*scale))
            pdb.gimp_file_save(img, img.active_layer, new_filename, '')
    # ユーザーが指定したフォルダが存在しないときは、警告を出す
    else:
        pdb.gimp_message("No such directory: %s" % (dirname))

register(
    "scale-batch",   # プロシジャの名前
    "Batch image scaler", # プロシジャの説明
    "", # PDBに登録する追加情報 
    "Yasushi Masuda", # プロシジャの作者
    "Placed on Public Domain.", # ライセンス情報
    "2008", # 作成日
    "ScaleBatch", # メニューに表示する名前
    "", # 対応する画像タイプ
    [(PF_DIRNAME, "directory", "Directory", os.getcwd()),
    (PF_STRING, "ext", "File extension, including dot", '.jpg'),
    (PF_STRING, "suffix", "Suffix for resized file", '_thumb'),
    (PF_FLOAT, "scale", "Scaling factor", 0.5)], # 引数定義
    [], # 戻り値定義
    do_scale_batch, # 処理する関数名
    menu="<Toolbox>/Xtns/MySample", # メニューを表示させる場所
)

main()
