## Modding SDK（必读）：

ATTENTION!: SDK适用加载器版本: 5.9.0 - 6.2.0

使用此模组时，必须遵守以下规则：

1. 如果要记录模块操作日志，请使用中文。

2. 必须更改__introduction__和__Supported_versions__ 并填写正确的值。

   文件在 Profiles/illustrate.py。

4. 如果可以使用 TTK 模块，使用 TTK，不要使用 TK。

5. 填写调用文件路径时，必须在前面加上 "mods/temp/mods/{打包的 zip 名称}/"，

    否则加载时会出错。

    例如：`path = 'mods/temp/mods/SDK/images/python.png'`。

    如果你这么写：`path = 'images/python.png'`，

    则会抛出FileNotFoundError错误。

7. 要调用本地模块/库，一定不要直接使用 `import library_name`，请使用：

    `from mods.temp.mods.<zip 名称> import repository_name`。

    原理与第四个问题相似。

9. 你可能需要你的模块名称稍微复杂一些，以避免与其他模块重名，因为

    用户无法重命名模块名称（这可能会导致错误）。

11. 你不需要任何构建工具来打包它，只需要将项目整个文件夹压缩成一个 zip 文件。

12. 如果要闭源，请前往 Profiles/command.py 并将__command_main__ 的值更改为你项目根目录中的 pyd 文件名字（无需后缀）。

13. 如果你的模组使用了第三方库，必须将Profiles/command.py的__command_libraries__和__command_libraries_name__更改，具体用法看文件注释。



## args 参数说明：

window_1: 添加和管理 GUI 组件的主窗口实例（如果不习惯可以改成root）。

    在这里，你可以将创建的 tkinter 组件传递给此窗口，就像这样：
    
        `ttk.Button(self.window_1, text='example').pack()`。
    
    这就像平常编写代码一样，只要在 window_1 上创建组件就可以。

button_1: “关于”选项的按钮。

    如果你想制作美化窗口工具可以将它进行美化。

logging_config: 包含日志配置的字典。模块应使用这些设置进行日志记录。

    可以使用print查看内容（前往 "load_mod" 并运行它！！！）。

error_detailed, error_name, error_simplification: 记录错误的变量。当错误发生时，mod加载器将更新这些列表。

    *⬇均为列表*
    
    error_detailed: 每个模块错误的详细信息。
    
    error_name: 所有出错模块的名称。
    
    error_simplification: 每个模块错误的简单信息。

    错误详细和错误简化，可以在下面自行打印查看区别。

loaded_mods: 用于记录成功加载模块的名称的列表。
    
    里面存放加载成功的列表。
