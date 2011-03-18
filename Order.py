#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import os, glob

def do_order_images(dirname, ext, w, h):
    # 指定のフォルダの有無を調べて、ファイルのリストを作成する
    # 順番はファイルの並び順なので、ファイル名を1***,2***にしておく
    if os.path.exists(dirname):
        img = gimp.Image(w, h)

        fnames = [f for f in glob.glob(os.path.join(dirname, '*'+ext))]

        for num, fname in enumerate(fnames):
            # ファイルを一つずつレイヤーとして開き、
            # TOOD:キャンバスサイズを横の大きさ分変えて右端に移動する
            lay = pdb.gimp_file_load_layer(img, fname)
            img.add_layer(lay)
            pdb.gimp_context_set_background((0,0,0))
            #pdb.gimp_image_set_active_layer(img, lay)
            pdb.gimp_image_resize(img, w + num*w, h, 0, 0)
            #pdb.gimp_layer_resize(lay, w, h, 0, 0)
            pdb.gimp_layer_set_offsets(lay, w*num, 0)
            #lay.translate(w, 0)
            #img.scale(int(img.width*scale), int(img.height*scale))
            #pdb.gimp_file_save(img, img.active_layer, new_filename, '')
        # 描画結果を表示する
        #pdb.gimp_image_flatten(img)
        # 結合するとalphaチャンネルが削除されるので、手動で頑張る
        #img.flatten()
        d = gimp.Display(img)

    # ユーザーが指定したフォルダが存在しないときは、警告を出す
    else:
        pdb.gimp_message("No such directory: %s" % (dirname))

register(
    "order-images",   # プロシジャの名前
    "Order images",   # プロシジャの説明
    "", # PDBに登録する追加情報 
    "Seitaro Ohno", # プロシジャの作者
    "Placed on Public Domain.", # ライセンス情報
    "2010", # 作成日
    "OrderImages", # メニューに表示する名前
    "", # 対応する画像タイプ
    [(PF_DIRNAME, "directory", "Directory", os.getcwd()),
    (PF_STRING, "ext", "File extension, including dot", '.png'),
    (PF_INT, "width", "Parameter width", 100),
    (PF_INT, "height", "Parameter height", 100)], # 引数定義
    [], # 戻り値定義
    do_order_images, # 処理する関数名
    menu="<Toolbox>/Xtns/MySample", # メニューを表示させる場所
)

main()
