# [`<span class="pre">os.path</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") --- 常用路径操作

**源代码：** [Lib/posixpath.py](https://github.com/python/cpython/tree/3.10/Lib/posixpath.py) （用于 POSIX）和 [Lib/ntpath.py](https://github.com/python/cpython/tree/3.10/Lib/ntpath.py) （用于 Windows NT）

---

该模块在路径名上实现了一些有用的功能：如需读取或写入文件，请参见 [`<span class="pre">open()</span>`](https://docs.python.org/zh-cn/3/library/functions.html#open "open") ；有关访问文件系统的信息，请参见 [`<span class="pre">os</span>`](https://docs.python.org/zh-cn/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") 模块。路径参数可以字符串或字节形式传递。我们鼓励应用程序将文件名表示为（Unicode）字符串。不幸的是，某些文件名在Unix上可能无法用字符串表示，因此在Unix上平台上需要支持任意文件名的应用程序，应使用字节对象来表示路径名。反之亦然，在Windows平台上仅使用字节对象，不能表示的所有文件名（以标准 `<span class="pre">mbcs</span>` 编码），因此Windows应用程序应使用字符串对象来访问所有文件。

与unix shell不同，Python不执行任何 *自动* 路径扩展。当应用程序需要类似shell的路径扩展时，可以显式调用诸如 [`<span class="pre">expanduser()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.expanduser "os.path.expanduser") 和 [`<span class="pre">expandvars()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.expandvars "os.path.expandvars") 之类的函数。 （另请参见 [`<span class="pre">glob</span>`](https://docs.python.org/zh-cn/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.") 模块。）

参见

[`<span class="pre">pathlib</span>`](https://docs.python.org/zh-cn/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths") 模块提供高级路径对象。

注解

所有这些函数都仅接受字节或字符串对象作为其参数。如果返回路径或文件名，则结果是相同类型的对象。

注解

由于不同的操作系统具有不同的路径名称约定，因此标准库中有此模块的几个版本。[`<span class="pre">os.path</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") 模块始终是适合 Python 运行的操作系统的路径模块，因此可用于本地路径。但是，如果操作的路径 *总是* 以一种不同的格式显示，那么也可以分别导入和使用各个模块。它们都具有相同的接口：

* `<span class="pre">posixpath</span>` 用于Unix 样式的路径
* `<span class="pre">ntpath</span>` 用于 Windows 路径

**在 3.8 版更改:** [`<span class="pre">exists()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.exists "os.path.exists")、[`<span class="pre">lexists()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.lexists "os.path.lexists")、[`<span class="pre">isdir()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.isdir "os.path.isdir")、[`<span class="pre">isfile()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.isfile "os.path.isfile")、[`<span class="pre">islink()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.islink "os.path.islink") 和 [`<span class="pre">ismount()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.ismount "os.path.ismount") 现在遇到系统层面上不可表示的字符或字节的路径时，会返回 `<span class="pre">False</span>`，而不是抛出异常。

`os.path.``abspath`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.abspath "永久链接至目标")返回路径 *path* 的绝对路径（标准化的）。在大多数平台上，这等同于用 `<span class="pre">normpath(join(os.getcwd(),</span><span> </span><span class="pre">path))</span>` 的方式调用 [`<span class="pre">normpath()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.normpath "os.path.normpath") 函数。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``basename`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.basename "永久链接至目标")返回路径 *path* 的基本名称。这是将 *path* 传入函数 [`<span class="pre">split()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.split "os.path.split") 之后，返回的一对值中的第二个元素。请注意，此函数的结果与Unix **basename** 程序不同。**basename** 在 `<span class="pre">'/foo/bar/'</span>` 上返回 `<span class="pre">'bar'</span>`，而 [`<span class="pre">basename()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.basename "os.path.basename") 函数返回一个空字符串 (`<span class="pre">''</span>`)。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``commonpath`( *paths* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.commonpath "永久链接至目标")接受包含多个路径的序列  *paths* ，返回 *paths* 的最长公共子路径。如果 *paths* 同时包含绝对路径和相对路径，或 *paths* 在不同的驱动器上，或 *paths* 为空，则抛出 [`<span class="pre">ValueError</span>`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError "ValueError") 异常。与 [`<span class="pre">commonprefix()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.commonprefix "os.path.commonprefix") 不同，本方法返回有效路径。

[可用性](https://docs.python.org/zh-cn/3/library/intro.html#availability): Unix, Windows。

**3.5 新版功能.**

**在 3.6 版更改:** 接受一个 [类路径对象](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object) 序列。

`os.path.``commonprefix`( *list* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.commonprefix "永久链接至目标")接受包含多个路径的  *列表* ，返回所有路径的最长公共前缀（逐字符比较）。如果 *列表* 为空，则返回空字符串 (`<span class="pre">''</span>`)。

注解

此函数是逐字符比较，因此可能返回无效路径。要获取有效路径，参见 [`<span class="pre">commonpath()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.commonpath "os.path.commonpath")。

**>>>**

```
>>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
'/usr/l'

>>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
'/usr'
```

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``dirname`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.dirname "永久链接至目标")返回路径 *path* 的目录名称。这是将 *path* 传入函数 [`<span class="pre">split()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.split "os.path.split") 之后，返回的一对值中的第一个元素。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``exists`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.exists "永久链接至目标")如果 *path* 指向一个已存在的路径或已打开的文件描述符，返回 `<span class="pre">True</span>`。对于失效的符号链接，返回 `<span class="pre">False</span>`。在某些平台上，如果使用 [`<span class="pre">os.stat()</span>`](https://docs.python.org/zh-cn/3/library/os.html#os.stat "os.stat") 查询到目标文件没有执行权限，即使 *path* 确实存在，本函数也可能返回 `<span class="pre">False</span>`。

**在 3.3 版更改:** *path* 现在可以是一个整数：如果该整数是一个已打开的文件描述符，返回 `<span class="pre">True</span>`，否则返回 `<span class="pre">False</span>`。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``lexists`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.lexists "永久链接至目标")如果 *path* 指向一个已存在的路径，返回 `<span class="pre">True</span>`。对于失效的符号链接，也返回 `<span class="pre">True</span>`。在缺失 [`<span class="pre">os.lstat()</span>`](https://docs.python.org/zh-cn/3/library/os.html#os.lstat "os.lstat") 的平台上等同于 [`<span class="pre">exists()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.exists "os.path.exists")。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``expanduser`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.expanduser "永久链接至目标")在 Unix 和 Windows 上，将参数中开头部分的 `<span class="pre">~</span>` 或 `<span class="pre">~user</span>` 替换为当前 *用户* 的家目录并返回。

在 Unix 上，开头的 `<span class="pre">~</span>` 会被环境变量 `<span class="pre">HOME</span>` 代替，如果变量未设置，则通过内置模块 [`<span class="pre">pwd</span>`](https://docs.python.org/zh-cn/3/library/pwd.html#module-pwd "pwd: The password database (getpwnam() and friends). (Unix)") 在 password 目录中查找当前用户的主目录。以 `<span class="pre">~user</span>` 开头则直接在 password 目录中查找。

在 Windows 上，如果 `<span class="pre">USERPROFILE</span>` 已设置将会被使用，否则 `<span class="pre">HOMEPATH</span>` 和 `<span class="pre">HOMEDRIVE</span>` 将被组合起来使用。 初始的 `<span class="pre">~user</span>` 会通过检查当前用户的家目录中匹配 `<span class="pre">USERNAME</span>` 的最后一部分目录名并执行替换来处理。

如果展开路径失败，或者路径不是以波浪号开头，则路径将保持不变。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

**在 3.8 版更改:** Windows 不再使用 `<span class="pre">HOME</span>`。

`os.path.``expandvars`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.expandvars "永久链接至目标")输入带有环境变量的路径作为参数，返回展开变量以后的路径。`<span class="pre">$name</span>` 或 `<span class="pre">${name}</span>` 形式的子字符串被环境变量 *name* 的值替换。格式错误的变量名称和对不存在变量的引用保持不变。

在 Windows 上，除了 `<span class="pre">$name</span>` 和 `<span class="pre">${name}</span>` 外，还可以展开 `<span class="pre">%name%</span>`。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``getatime`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.getatime "永久链接至目标")返回 *path* 的最后访问时间。返回值是一个浮点数，为纪元秒数（参见 [`<span class="pre">time</span>`](https://docs.python.org/zh-cn/3/library/time.html#module-time "time: Time access and conversions.") 模块）。如果该文件不存在或不可访问，则抛出 [`<span class="pre">OSError</span>`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError "OSError") 异常。

`os.path.``getmtime`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.getmtime "永久链接至目标")返回 *path* 的最后修改时间。返回值是一个浮点数，为纪元秒数（参见 [`<span class="pre">time</span>`](https://docs.python.org/zh-cn/3/library/time.html#module-time "time: Time access and conversions.") 模块）。如果该文件不存在或不可访问，则抛出 [`<span class="pre">OSError</span>`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError "OSError") 异常。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``getctime`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.getctime "永久链接至目标")返回 *path* 在系统中的 ctime，在有些系统（比如 Unix）上，它是元数据的最后修改时间，其他系统（比如 Windows）上，它是 *path* 的创建时间。返回值是一个数，为纪元秒数（参见 [`<span class="pre">time</span>`](https://docs.python.org/zh-cn/3/library/time.html#module-time "time: Time access and conversions.") 模块）。如果该文件不存在或不可访问，则抛出 [`<span class="pre">OSError</span>`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError "OSError") 异常。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``getsize`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.getsize "永久链接至目标")返回 *path* 的大小，以字节为单位。如果该文件不存在或不可访问，则抛出 [`<span class="pre">OSError</span>`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError "OSError") 异常。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``isabs`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.isabs "永久链接至目标")如果 *path* 是一个绝对路径，则返回 `<span class="pre">True</span>`。在 Unix 上，它就是以斜杠开头，而在 Windows 上，它可以是去掉驱动器号后以斜杠（或反斜杠）开头。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``isfile`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.isfile "永久链接至目标")如果 *path* 是 [`<span class="pre">现有的</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.exists "os.path.exists") 常规文件，则返回 `<span class="pre">True</span>`。本方法会跟踪符号链接，因此，对于同一路径，[`<span class="pre">islink()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.islink "os.path.islink") 和 [`<span class="pre">isfile()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.isfile "os.path.isfile") 都可能为 `<span class="pre">True</span>`。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``isdir`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.isdir "永久链接至目标")如果 *path* 是 [`<span class="pre">现有的</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.exists "os.path.exists") 目录，则返回 `<span class="pre">True</span>`。本方法会跟踪符号链接，因此，对于同一路径，[`<span class="pre">islink()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.islink "os.path.islink") 和 [`<span class="pre">isdir()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.isdir "os.path.isdir") 都可能为 `<span class="pre">True</span>`。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``islink`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.islink "永久链接至目标")如果 *path* 指向的 [`<span class="pre">现有</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.exists "os.path.exists") 目录条目是一个符号链接，则返回 `<span class="pre">True</span>`。如果 Python 运行时不支持符号链接，则总是返回 `<span class="pre">False</span>`。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``ismount`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.ismount "永久链接至目标")如果路径 *path* 是 *挂载点* （文件系统中挂载其他文件系统的点），则返回 `<span class="pre">True</span>`。在 POSIX 上，该函数检查 *path* 的父目录 `<em><span class="pre">path</span></em><span class="pre">/..</span>` 是否在与 *path* 不同的设备上，或者 `<em><span class="pre">path</span></em><span class="pre">/..</span>` 和 *path* 是否指向同一设备上的同一 inode（这一检测挂载点的方法适用于所有 Unix 和 POSIX 变体）。本方法不能可靠地检测同一文件系统上的绑定挂载 (bind mount)。在 Windows 上，盘符和共享 UNC 始终是挂载点，对于任何其他路径，将调用 `<span class="pre">GetVolumePathName</span>` 来查看它是否与输入的路径不同。

**3.4 新版功能:** 支持在 Windows 上检测非根挂载点。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``join`( *path* ,  ****paths*** **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.join "永久链接至目标")智能地拼接一个或多个路径部分。 返回值是 *path* 和 **paths* 的所有成员的拼接，其中每个非空部分后面都紧跟一个目录分隔符，最后一个部分除外，这意味着如果最后一个部分为空，则结果将以分隔符结尾。 如果某个部分为绝对路径，则之前的所有部分会被丢弃并从绝对路径部分开始继续拼接。

在 Windows 上，遇到绝对路径部分（例如 `<span class="pre">r'\foo'</span>`）时，不会重置盘符。如果某部分路径包含盘符，则会丢弃所有先前的部分，并重置盘符。请注意，由于每个驱动器都有一个“当前目录”，所以 `<span class="pre">os.path.join("c:",</span><span> </span><span class="pre">"foo")</span>` 表示驱动器 `<span class="pre">C:</span>` 上当前目录的相对路径 (`<span class="pre">c:foo</span>`)，而不是 `<span class="pre">c:\foo</span>`。

**在 3.6 版更改:** 接受一个 [类路径对象](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object) 用于 *path* 和 *paths* 。

`os.path.``normcase`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.normcase "永久链接至目标")规范路径的大小写。在 Windows 上，将路径中的所有字符都转换为小写，并将正斜杠转换为反斜杠。在其他操作系统上返回原路径。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``normpath`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.normpath "永久链接至目标")> 通过折叠多余的分隔符和对上级目录的引用来标准化路径名，所以 `<span class="pre">A//B</span>`、`<span class="pre">A/B/</span>`、`<span class="pre">A/./B</span>` 和 `<span class="pre">A/foo/../B</span>` 都会转换成 `<span class="pre">A/B</span>`。这个字符串操作可能会改变带有符号链接的路径的含义。在 Windows 上，本方法将正斜杠转换为反斜杠。要规范大小写，请使用 [`<span class="pre">normcase()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.normcase "os.path.normcase")。

注解

> 在 POSIX 系统上，根据 [IEEE Std 1003.1 2013 Edition; 4.13 Pathname Resolution](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_13)，如果一个路径名称以两个斜杠开始，则开始字符之后的第一个部分将以具体实现所定义的方式来解读，但是超过两个开始字符则将被视为单个字符。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``realpath`( *path* ,  *** ,  *strict**=**False* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.realpath "永久链接至目标")返回指定文件的规范路径，消除路径中存在的任何符号链接（如果操作系统支持）。

如果一个路径不存在或是遇到了符号链接循环，并且 *strict* 为 `<span class="pre">True</span>`，则会引发 [`<span class="pre">OSError</span>`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError "OSError")。 如果 *strict* 为 `<span class="pre">False</span>`，则会尽可能地解析路径并添加结果而不检查路径是否存在。

注解

这个函数会模拟操作系统生成规范路径的过程，Windows 与 UNIX 的这个过程在处理链接和后续路径组成部分的交互方式上有所差异。

操作系统 API 会根据需要来规范化路径，因此通常不需要调用此函数。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

**在 3.8 版更改:** 在 Windows 上现在可以正确解析符号链接和交接点 (junction point)。

**在 3.10 版更改:** 增加了 *strict* 形参。

`os.path.``relpath`( *path* ,  *start**=**os.curdir* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.relpath "永久链接至目标")返回从当前目录或可选的 *start* 目录至 *path* 的相对文件路径。 这只是一个路径计算：不会访问文件系统来确认 *path* 或 *start* 是否存在或其性质。 在 Windows 上，当 *path* 和 *start* 位于不同驱动器时将引发 [`<span class="pre">ValueError</span>`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError "ValueError")。

*start* 默认为 [`<span class="pre">os.curdir</span>`](https://docs.python.org/zh-cn/3/library/os.html#os.curdir "os.curdir")。

[可用性](https://docs.python.org/zh-cn/3/library/intro.html#availability): Unix, Windows。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``samefile`( *path1* ,  *path2* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.samefile "永久链接至目标")如果两个路径都指向相同的文件或目录，则返回 `<span class="pre">True</span>`。这由设备号和 inode 号确定，在任一路径上调用 [`<span class="pre">os.stat()</span>`](https://docs.python.org/zh-cn/3/library/os.html#os.stat "os.stat") 失败则抛出异常。

[可用性](https://docs.python.org/zh-cn/3/library/intro.html#availability): Unix, Windows。

**在 3.2 版更改:** 添加了对 Windows 的支持。

**在 3.4 版更改:** Windows现在使用与其他所有平台相同的实现。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``sameopenfile`( *fp1* ,  *fp2* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.sameopenfile "永久链接至目标")如果文件描述符 *fp1* 和 *fp2* 指向相同文件，则返回 `<span class="pre">True</span>`。

[可用性](https://docs.python.org/zh-cn/3/library/intro.html#availability): Unix, Windows。

**在 3.2 版更改:** 添加了对 Windows 的支持。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``samestat`( *stat1* ,  *stat2* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.samestat "永久链接至目标")如果 stat 元组 *stat1* 和 *stat2* 指向相同文件，则返回 `<span class="pre">True</span>`。这些 stat 元组可能是由 [`<span class="pre">os.fstat()</span>`](https://docs.python.org/zh-cn/3/library/os.html#os.fstat "os.fstat")、[`<span class="pre">os.lstat()</span>`](https://docs.python.org/zh-cn/3/library/os.html#os.lstat "os.lstat") 或 [`<span class="pre">os.stat()</span>`](https://docs.python.org/zh-cn/3/library/os.html#os.stat "os.stat") 返回的。本函数实现了 [`<span class="pre">samefile()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.samefile "os.path.samefile") 和 [`<span class="pre">sameopenfile()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.sameopenfile "os.path.sameopenfile") 底层所使用的比较过程。

[可用性](https://docs.python.org/zh-cn/3/library/intro.html#availability): Unix, Windows。

**在 3.4 版更改:** 添加了对 Windows 的支持。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``split`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.split "永久链接至目标")将路径 *path* 拆分为一对，即 `<span class="pre">(head,</span><span> </span><span class="pre">tail)</span>`，其中，*tail* 是路径的最后一部分，而 *head* 里是除最后部分外的所有内容。*tail* 部分不会包含斜杠，如果 *path* 以斜杠结尾，则 *tail* 将为空。如果 *path* 中没有斜杠，*head* 将为空。如果 *path* 为空，则 *head* 和 *tail* 均为空。*head* 末尾的斜杠会被去掉，除非它是根目录（即它仅包含一个或多个斜杠）。在所有情况下，`<span class="pre">join(head,</span><span> </span><span class="pre">tail)</span>` 指向的位置都与 *path* 相同（但字符串可能不同）。另请参见函数 [`<span class="pre">dirname()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.dirname "os.path.dirname") 和 [`<span class="pre">basename()</span>`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.basename "os.path.basename")。

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``splitdrive`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.splitdrive "永久链接至目标")将路径 *path* 拆分为一对，即 `<span class="pre">(drive,</span><span> </span><span class="pre">tail)</span>`，其中 *drive* 是挂载点或空字符串。在没有驱动器概念的系统上，*drive* 将始终为空字符串。在所有情况下，`<span class="pre">drive</span><span> </span><span class="pre">+</span><span> </span><span class="pre">tail</span>` 都与 *path* 相同。

在 Windows 上，本方法将路径拆分为驱动器/UNC 根节点和相对路径。

如果路径 path 包含盘符，则 drive 将包含冒号之前的所有内容包括冒号本身:

**>>>**

```
>>> splitdrive("c:/dir")
("c:", "/dir")
```

如果路径 path 包含 UNC 路径，则 drive 将包含主机名和 share，直至第四个分隔符但不包括该分隔符:

**>>>**

```
>>> splitdrive("//host/computer/dir")
("//host/computer", "/dir")
```

**在 3.6 版更改:** 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

`os.path.``splitext`( *path* **)**[](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.splitext "永久链接至目标")将路径名称 *path* 拆分为 `<span class="pre">(root,</span><span> </span><span class="pre">ext)</span>` 对使得 `<span class="pre">root</span><span> </span><span class="pre">+</span><span> </span><span class="pre">ext</span><span> </span><span class="pre">==</span><span> </span><span class="pre">path</span>`，并且扩展名 *ext* 为空或以句点打头并最多只包含一个句点。

如果路径 path 不包含扩展名，则 *ext* 将为 `<span class="pre">''</span>`:

```
>>> splitext('bar')
('bar', '')
```

如果路径 path 包含扩展名，则 *ext* 将被设为该扩展名，包括打头的句点。 请注意在其之前的句点将被忽略:

**>>>**

```
>>> splitext('foo.bar.exe')
('foo.bar', '.exe')
```

基本名中打头的句点会被忽略:

**>>>**

```
>>> splitext('.cshrc')
('.cshrc', '')
```
