**Modding SDK(v6.7.2)**（必读）：

使用此脚本时，请遵守以下规则：

1. 如果您要记录模块操作日志，请使用中文。

2. 您必须更改 __introduction__ 和 __Supported_versions__ 并填写正确的值。
    请在 Profiles/illustrate 目录中进行。

3. 如果可以使用 TTK 模块，请使用 TTK，不要使用 TK。

4. 填写调用文件路径时，必须在前面加上 "mods/temp/mods/{打包的 zip 名称}/"，
    否则加载时会出错。
    例如：`path = 'mods/temp/mods/SDK/images/python.png'`。
    如果您正常编写，应该写成：`path = 'images/python.png'`。

5. 要调用本地模块/库，请不要直接使用 `import library_name`，请使用：
    `from mods.temp.mods.<zip 名称> import repository_name`。

6. 您可能需要使您的模块名称稍微复杂一些，以避免与其他模块重名，主要是因为
    用户无法重命名模块名称（这可能会导致错误）。我真的不想制定这个规则。。。

7. 您不需要任何构建工具来打包它，只需直接将其压缩成一个 zip 文件，
    放在项目的根目录即可。

8. 如果您希望关闭源代码，请前往 Profiles/command 并将 __command_main__ 的值更改为您项目根目录中的 pyd 文件
    （无需后缀）。

args 参数说明：

window_1: 添加和管理 GUI 组件的主窗口实例（这也是您最常使用的窗口）。
    在这里，您可以将您创建的 tkinter 组件传递给此窗口，就像这样：
        `ttk.Button(self.window_1, text='example').pack()`。
    这就像平常编写代码一样，只需在 window_1 上创建组件即可。

button_1: 按钮的实例，模块可以使用它来添加事件处理程序。
    此按钮用于开发人员测试，即仅用于测试更改按钮内容的内容（也可以隐藏），
    它也作为开发者方法来更改组件。

logging_config: 包含日志配置的字典。模块应使用这些设置进行日志记录。
    您可以在主函数中看到如何使用它的详细信息，也可以使用 print 
    查看内容（前往 "加载 mod" 并运行它！！！）。

error_detailed, error_name, error_simplification: 记录错误的变量。当错误发生时，
    模块应更新这些变量。
    error_detailed: 每个模块错误的详细信息，是一个列表。
    error_name: 所有出错模块的名称。
    error_simplification: 每个模块错误的简单信息。

    错误详细和错误简化，您可以在下面自行打印以查看区别。

loaded_mods: 用于记录成功加载模块的名称的列表。
    里面存放的是加载成功的列表。
