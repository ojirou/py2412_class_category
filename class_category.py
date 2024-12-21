import os
import shutil

# 入力プロンプトでフォルダを指定
input_folder = input("整理するフォルダのパスを入力してください: ")

if not os.path.exists(input_folder):
    print(f"指定されたフォルダが存在しません: {input_folder}")
else:
    files = os.listdir(input_folder)
    for file in files:
        # ファイル名からカテゴリを取得
        category = '_'.join(file.split('_')[:-1])

        # カテゴリフォルダのパスを生成
        category_folder = os.path.join(input_folder, category)

        # フォルダが存在しない場合は作成
        if not os.path.exists(category_folder):
            os.mkdir(category_folder)
        else:
            print(f'すでにフォルダが存在します: {category_folder}')

        # ファイルをカテゴリフォルダに移動
        shutil.move(os.path.join(input_folder, file), os.path.join(category_folder, file))

    print("ファイルの整理が完了しました。")
