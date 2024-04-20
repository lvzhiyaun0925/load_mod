# 不要更改变量名，SDK将不生效！！
# 本文件的代码始终为最新版本
import _tkinter
import importlib
import json
import os
import re
import sys
import time
import tkinter as tk
import webbrowser
import traceback
import logging
import zipfile
import shutil
import requests
import markdown
import io
import pickle
from pip._internal import main as pip_main
from tkinter import ttk, messagebox
from tkhtmlview import HTMLLabel
from datetime import datetime
from ttkthemes import ThemedStyle
version = '6.2.0'  # app version

file__name = f'logs/{datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d_%H-%M-%S")}_log.log'

logging_config = {
    'filename': file__name,
    'level': logging.DEBUG,
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'encoding': 'utf-8'
}

try:

    with open(logging_config['filename'], 'w'):
        pass
except FileNotFoundError:

    os.mkdir('logs')
    with open(logging_config['filename'], 'w'):
        pass

logging.basicConfig(filename=logging_config['filename'], level=logging_config['level'], format=logging_config['format'],
                    encoding='utf-8')


drag_start_x, drag_start_y = 0, 0


def on_drag_start(event):
    global drag_start_x, drag_start_y
    drag_start_x = event.x
    drag_start_y = event.y


def on_drag_motion(event, root):
    x = root.winfo_x() + event.x - drag_start_x
    y = root.winfo_y() + event.y - drag_start_y
    root.geometry(f"+{x}+{y}")


def button_1_command(_id=0):
    def download():
        if os.path.basename(sys.argv[0]) == 'load_mod.pyw':
            _r = requests.get('https://gitcode.net/lvzhiyuan_0925/my_version/-/raw/master/apps/load_mod.pyw')

            with open('load_mod.pyw', 'wb') as _file:
                _file.write(_r.content)

        elif os.path.basename(sys.argv[0]) == 'load_mod.exe':
            _r = requests.get('https://gitcode.net/lvzhiyuan_0925/my_version/-/raw/master/apps/load_mod.exe')

            with open('load_mod.exe', 'wb') as _file:
                _file.write(_r.content)

        else:

            messagebox.showerror('？？', '?????')
            return

        messagebox.showwarning('更新完成', '更新完成， 重启应用以完成更新')
    root = tk.Toplevel(i)
    if _id == 0:
        root.title("关于")

    elif _id == 1:
        root.title('使用教程')

    else:
        raise TypeError(f'_id arg do not have {_id}')
    label = tk.Label(root, text='获取中请稍后...')
    label.pack()
    root.update()
    try:
        if _id == 0:
            r = requests.get('https://gitcode.net/lvzhiyuan_0925/my_version/-/raw/master/version.json')
            data = json.loads(r.text)['version']
            r = requests.get(f'https://gitcode.net/lvzhiyuan_0925/my_version/-/raw/master/{data}.md')
            label.destroy()

        elif _id == 1:
            r = requests.get('https://gitcode.net/lvzhiyuan_0925/my_version/-/raw/master/tutorial.md')
            label.destroy()

        else:
            raise TypeError(f'_id arg do not have {_id}')
    except requests.exceptions.ConnectionError:
        label.config(text=f'获取失败:')
        tk.Label(root, text='网络错误', fg='red').pack()
        ttk.Button(root, text='重试', command=lambda: (root.destroy(), button_1_command()), style='Custom.TButton').pack()
        return
    except Exception as e:
        label.config(text=f'获取失败:')
        tk.Label(root, text=str(e), fg='red').pack()
        ttk.Button(root, text='重试', command=lambda: (root.destroy(), button_1_command()), style='Custom.TButton').pack()
        return

    data = r.text
    del r
    html_content = markdown.markdown(data)

    html_label = HTMLLabel(root, html=html_content)
    scrollbar = ttk.Scrollbar(root, command=html_label.yview)
    scrollbar.pack(side="right", fill="y")
    html_label.config(yscrollcommand=scrollbar.set)
    html_label.pack(fill="both", expand=True)
    del html_label, data
    try:
        r = requests.get('https://gitcode.net/lvzhiyuan_0925/my_version/-/raw/master/version.json')
        data = json.loads(r.text)['version']

        _version = int(re.sub(r'\.', '', version))  # Here it is removed with a regular expression".".
        _new_version = int(re.sub(r'\.', '', data))
        del r

        if _version == _new_version:
            ttk.Button(root, text=f'最新版本: 已经是最新版本', command=lambda: messagebox.
                       showinfo('提示', '目前最新版本'), style='Custom.TButton').pack()

        elif _version < _new_version:
            ttk.Button(root, text=f'最新版本: {data}(点击更新)', command=download, style='Custom.TButton').pack()

        del _version, _new_version
    except requests.exceptions.ProxyError as e:
        ttk.Button(root, text=f'最新版本: 获取错误:\n{e}', style='Custom.TButton').pack()
    except requests.exceptions.ConnectionError as e:
        ttk.Button(root, text=f'最新版本: 获取错误:\n{e}', style='Custom.TButton').pack()

    ttk.Button(root, text='使用教程', command=lambda: button_1_command(1), style='Custom.TButton').pack()
    ttk.Button(root, text='联系作者', command=lambda: webbrowser.open('mailto:lvzhiyuan0925@outlook.com'),
               style='Custom.TButton').pack()
    label = tk.Label(root, text=f'当前版本: {version}', fg='blue', cursor='hand2')
    label.pack()
    label.bind('<Button-1>', lambda event: webbrowser.open(f'https://gitcode.net/lvzhiyuan_0925/m'
                                                           f'y_version/-/blob/master/{version}.md'))
    root.mainloop()


i = tk.Tk()
try:
    with open('data.pkl', 'rb') as __file:
        try:
            _data = pickle.load(__file)
            ThemedStyle().set_theme(_data)
            del _data

        except (KeyError, EOFError, _tkinter.TclError):
            ThemedStyle().set_theme('radiance')
            open('data.pkl', 'w').close()

except FileNotFoundError:
    open('data.pkl', 'w').close()
    ThemedStyle().set_theme('radiance')

logging.info(f'-创建窗口-')

error_1 = []
error_1_j = []
error_name = []
mod_list = []
mod_list_error = []
mod_name = []  # Doesn't count loading errors.

folder_path = 'mods/'


def mod_run():
    global folder_path
    try:
        os.mkdir('mods')
        os.mkdir('mods/libraries')
        (ttk.Label(i, text='[###来自安装包的话###]\n'
                           '初次使用，是吧？\n我们已为你初始化，现在，在应用程序\n目录下，有一个mods文件夹，请把你要加载的模组丢进去(.zip)，'
                           '\n然后重启此应用(你可以在关于页面看到详细的教程(当然是最新版本的))\n'
                           '初次加载模组可能会碰到下载必要库的情况，这属于正常现象，等待下载完成即可\n'
                           '等你放上模组并且加载成功后，你会在mods文件夹下见到一个temp文件夹，\n模组解压后的文件就放在temp/mods下\n'
                           '但是他会在你每次启动应用时删了重新解压，所以，叫做temp文件夹。\n不要改模组的名称！！！！一定一定')
         .pack())
        ttk.Button(i, text='退出（然后自己重新点开应用以加载模组）', command=lambda: sys.exit()).pack()
        i.mainloop()

    except FileExistsError:
        pass
    button_1 = ttk.Button(text='关于', command=button_1_command)
    button_1.pack()

    try:
        # That is, each load will first empty the folder and re-decompress it
        shutil.rmtree(f'mods/temp/mods')
    except FileNotFoundError:

        pass

    folder_path = 'mods/'
    for entry in os.listdir(folder_path):
        logging.info(f'扫描{entry}:')
        entry_path = os.path.join(folder_path, entry)
        file_name, file_extension = os.path.splitext(entry_path)

        if file_extension == '.zip':
            logging.info(f'\t正在尝试加载({entry})')
            logging.info(f'\t正在解压')
            with zipfile.ZipFile(entry_path, 'r') as zip_file:
                zip_file.extractall(f'mods/temp/{file_name}/')
            logging.info(f'\t解压完成')
            entry_path = f'mods/temp/{file_name}/Profiles/command'
            modified_string = entry_path.replace('/', '.')
            path = modified_string
            mods = importlib.import_module(path)
            logging.info('\t加载配置文件完成')
            entry_path = f'mods/temp/{file_name}/{mods.__command_main__}'
            modified_string = entry_path.replace('/', '.')
            path = modified_string
            del modified_string

            try:

                mod_name.append(path)
                lack = list(set(mods.__command_libraries_name__) - set(os.listdir('mods/libraries/')))
                logging.info('\t缺失库:{}'.format(f'{lack}, 正在下载并安装' if lack is not [] else '无'))

                for _ in lack:
                    __ = _  # preventDuplicateNames
                    logging.warning(f'\t\t正在下载缺失库:{_}')
                    window = tk.Toplevel(i)

                    ttk.Label(window, text='我们正在下载mod所需的库(没响应正常，懒得多线程，请勿关闭)，请稍后...').pack()

                    progress_frame = ttk.Frame(window)
                    progress_frame.pack(pady=20)
                    progress_bar = ttk.Progressbar(progress_frame, orient='horizontal', length=200, mode='determinate')
                    progress_bar.pack(pady=10)

                    window.update()

                    try:

                        os.mkdir(f'mods/libraries/'
                                 f'{mods.__command_libraries[mods.__command_libraries_name__.index(_)]}')

                    except FileExistsError:
                        pass

                    value = progress_bar["value"] + 10
                    progress_bar["value"] = value
                    window.update()
                    original_stderr = sys.stderr

                    sys.stderr = io.StringIO()
                    pip_main(['install', '--target', f'mods/libraries/'
                             f'{mods.__command_libraries_name__[mods.__command_libraries_name__.index(_)]}', _])
                    sys.stderr = original_stderr
                    value = progress_bar["value"] + 90
                    progress_bar["value"] = value
                    window.update()
                    window.destroy()
                    logging.info(f'\t\t已下载并安装缺失库:{__}')
                    del __
                for _ in os.listdir('mods/libraries/'):
                    if _ not in sys.path:
                        if _ != '':
                            try:
                                (sys.path.append
                                 (f'{os.getcwd()}\\mods\\libraries\\'
                                  f'{mods.__command_libraries_name__[mods.__command_libraries_name__.index(_)]}'))

                            except ValueError:
                                continue

                _mod = importlib.import_module(path)
                run = (f'_mod.{mods.__command_class__}({mods.__command_class_args__}).{mods.__command_function__}'
                       f'({mods.__command_function_args__}){mods.__command_append__}')
                exec(run)
                mod_list.append(entry_path)
                logging.info('\tmod加载成功')

            except Exception as error:
                logging.error('------------------------------------')
                logging.error(f'加载{entry_path}时出现错误')

                error_name.append(path)
                _error = traceback.format_exc()
                error_1_j.append(str(error))
                error_1.append(str(_error))
                mod_list_error.append(f'{entry_path}')
                logging.error(
                    f'简化:{str(error)}\n详细{str(_error)}\n'
                    '------------------------------------'
                )
                messagebox.showinfo('加载mod失败', f'mod加载失败，以下为错误报告：\n{_error}\n\n已记录到log.log')

        elif os.path.isfile(entry_path) and file_extension == '.false':
            logging.warning('这是一个被标记为不加载的mod，将不加载')

        elif os.path.isfile(entry_path) and file_extension != '.zip':
            logging.error('?这个mod后缀不是.zip，将不加载')


def button_2_command():

    def personalize():
        root_2 = tk.Toplevel(root)

        def close_window():
            if messagebox.askyesno('是否保存', '是否保存'):
                r()
            else:
                root_2.destroy()

        def r():
            with open('data.pkl', 'wb') as file:
                _ = combobox.get()
                pickle.dump(_, file)
                del _
            root_2.destroy()
            if messagebox.askyesno('设置', '个性化功能需要重启应用以完成加载，是否重启?'):
                os.startfile(os.path.abspath(__file__))
                sys.exit()

        ttk.Label(root_2, text='下拉选择界面样式').pack()
        pixmap_themes = [
            "arc",
            "blue",
            "clearlooks",
            "elegance",
            "kroc",
            "plastik",
            "radiance",
            "ubuntu",
            "winxpblue"
        ]

        combobox = ttk.Combobox(root_2, values=pixmap_themes)

        with open('data.pkl', 'rb') as _file:
            try:
                data = pickle.load(_file)
                if data in pixmap_themes:
                    combobox.set(data)

                else:
                    combobox.set('radiance')

            except (KeyError, EOFError):
                combobox.set('radiance')
        combobox.pack()

        ttk.Button(root_2, text='确定', command=r).pack()
        del pixmap_themes
        root_2.title('设置-个性化')
        root_2.protocol('WM_DELETE_WINDOW', close_window)
        root_2.mainloop()

    root = tk.Toplevel(i)
    ttk.Button(root, text='个性化', command=personalize).pack()

    root.title('设置')
    root.mainloop()


i.title('工具箱')

mod_run()

logging.info('--mod加载完成--')
logging.info(f'正确加载模组:{mod_list},数量:{len(mod_list)}')
logging.info(f'未正确加载模组:{mod_list_error},数量:{len(mod_list_error)}')
logging.info(f'合计:{len(mod_list) + len(mod_list_error)}个,正确加载模组数量:'
             f'{len(mod_list)},未正确加载模组数量:{len(mod_list_error)}')
logging.info(f'-以下记录用户操作-')

ttk.Button(i, text='设置', command=button_2_command).pack()

del error_1, error_1_j, error_name, mod_list, mod_list_error, mod_name, folder_path, logging_config

try:

    i.mainloop()
except KeyboardInterrupt:
    pass
