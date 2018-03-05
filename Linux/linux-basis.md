## linux入门
### 启动
linux启动分五步

#### 1.内核的引导
1. 当计算机打开电源后，首先是BIOS开机自检，按照BIOS中设置的启动设备（通常是硬盘）来启动。
2. 紧接着由启动设备上的grub程序开始引导linux，
3. 当引导程序成功完成引导任务后，
4. Linux从它们手中接管了CPU的控制权，然后CPU就开始执行Linux的核心映象代码，开始了Linux启动过程。
5. 也就是所谓的内核引导开始了，在内核引导过程中其实是很复杂的，我们就当它是一个黑匣子，反正是linux内核做了一系列工作，最后内核调用加载了init程序，至此内核引导的工作就完成了。

#### 2. 运行init
1. init 进程是系统所有进程的起点，你可以把它比拟成系统所有进程的老祖宗，没有这个进程，系统中任何进程都不会启动。
2. init 程序首先是需要读取配置文件 /etc/inittab。inittab是一个不可执行的文本文件，它有若干行指令所组成。
3. （你可以在你的linux上执行命令 cat /etc/inittab 这样获得）

	```
	# inittab       This file describes how the INIT process should set up
	#               the system in a certain run-level.
	#
	# Author:       Miquel van Smoorenburg,
	#               Modified for RHS Linux by Marc Ewing and Donnie Barnes
	#
	# Default runlevel. The runlevels used by RHS are:
	#   0 - halt (Do NOT set initdefault to this)
	#   1 - Single user mode
	#   2 - Multiuser, without NFS (The same as 3, if you do not havenetworking)
	#   3 - Full multiuser mode
	#   4 - unused
	#   5 - X11
	#   6 - reboot (Do NOT set initdefault to this)
	#
	###表示当前缺省运行级别为5(initdefault)；
	id:5:initdefault:
	###启动时自动执行/etc/rc.d/rc.sysinit脚本(sysinit)
	# System initialization.
	si::sysinit:/etc/rc.d/rc.sysinit
	l0:0:wait:/etc/rc.d/rc 0
	l1:1:wait:/etc/rc.d/rc 1
	l2:2:wait:/etc/rc.d/rc 2
	l3:3:wait:/etc/rc.d/rc 3
	l4:4:wait:/etc/rc.d/rc 4
	###当运行级别为5时，以5为参数运行/etc/rc.d/rc脚本，init将等待其返回(wait)
	l5:5:wait:/etc/rc.d/rc 5
	l6:6:wait:/etc/rc.d/rc 6
	###在启动过程中允许按CTRL-ALT-DELETE重启系统
	# Trap CTRL-ALT-DELETE
	ca::ctrlaltdel:/sbin/shutdown -t3 -r now
	# When our UPS tells us power has failed, assume we have a few minutes
	# of power left.  Schedule a shutdown for 2 minutes from now.
	# This does, of course, assume you have powerd installed and your
	# UPS connected and working correctly.
	pf::powerfail:/sbin/shutdown -f -h +2 "Power Failure; System Shutting Down"
	# If power was restored before the shutdown kicked in, cancel it.
	pr:12345:powerokwait:/sbin/shutdown -c "Power Restored; Shutdown Cancelled"
	###在2、3、4、5级别上以ttyX为参数执行/sbin/mingetty程序，打开ttyX终端用于用户登录，
	###如果进程退出则再次运行mingetty程序(respawn)
	# Run gettys in standard runlevels
	1:2345:respawn:/sbin/mingetty tty1
	2:2345:respawn:/sbin/mingetty tty2
	3:2345:respawn:/sbin/mingetty tty3
	4:2345:respawn:/sbin/mingetty tty4
	5:2345:respawn:/sbin/mingetty tty5
	6:2345:respawn:/sbin/mingetty tty6
	###在5级别上运行xdm程序，提供xdm图形方式登录界面，并在退出时重新执行(respawn)
	# Run xdm in runlevel 5
	x:5:respawn:/etc/X11/prefdm -nodaemon
	```

- 以上面的inittab文件为例，来说明一下inittab的格式。其中以#开始的行是注释行，除了注释行之外，每一行都有以下格式： 
	- id:runlevel:action:process
	- 对上面各项的详细解释如下：
		1. id
			- id是指入口标识符，它是一个字符串，对于getty或mingetty等其他login程序项，要求id与tty的编号相同，否则getty程序将不能正常工作。
		2. Runlevel
			- runlevel是init所处于的运行级别的标识，一般使用0－6以及S或s。
			- 0、1、6运行级别被系统保留：其中0作为shutdown动作，1作为重启至单用户模式，6为重启；S和s意义相同，表示单用户模式，且无需inittab文件，因此也不在inittab中出现，实际上，进入单用户模式时，init直接在控制台（/dev/console）上运行/sbin/sulogin。
			- 在一般的系统实现中，都使用了2、3、4、5几个级别，在CentOS系统中，2表示无NFS支持的多用户模式，3表示完全多用户模式（也是最常用的级别），4保留给用户自定义，5表示XDM图形登录方式。
			- 7－9级别也是可以使用的，传统的Unix系统没有定义这几个级别。
			- runlevel可以是并列的多个值，以匹配多个运行级别，对大多数action来说，仅当runlevel与当前运行级别匹配成功才会执行。
		3. action
			- action是描述其后的process的运行方式的。
			- action可取的值包括：initdefault、sysinit、boot、bootwait等：　initdefault是一个特殊的action值，用于标识缺省的启动级别；当init由核心激活以后，它将读取inittab中的initdefault项，取得其中的runlevel，并作为当前的运行级别。
			- 如果没有inittab文件，或者其中没有initdefault项，init将在控制台上请求输入runlevel。
			- sysinit、boot、bootwait等action将在系统启动时无条件运行，而忽略其中的runlevel。
			- 其余的action（不含initdefault）都与某个runlevel相关。
			- 各个action的定义在inittab的man手册中有详细的描述。
		4. process
			- process为具体的执行程序。程序后面可以带参数。 

>Tips: 如果你看不懂这个文件，没有关系，随着你对linux的深入了解，你再回过头看这个文件你就会豁然开朗的。但是你现在必须要明白runlevel的各个级别的含义。


#### 3. 系统初始化
- 在init的配置文件中有这么一行： si::sysinit:/etc/rc.d/rc.sysinit　它调用执行了/etc/rc.d/rc.sysinit，而rc.sysinit是一个bash shell的脚本，它主要是完成一些系统初始化的工作，rc.sysinit是每一个运行级别都要首先运行的重要脚本。它主要完成的工作有：激活交换分区，检查磁盘，加载硬件模块以及其它一些需要优先执行任务。
- rc.sysinit约有850多行，但是每个单一的功能还是比较简单，而且带有注释，建议有兴趣的用户可以自行阅读自己机器上的该文件，以了解系统初始化所详细情况。由于此文件较长，所以不在本文中列出来，也不做具体的介绍。当rc.sysinit程序执行完毕后，将返回init继续下一步。通常接下来会执行到/etc/rc.d/rc程序。以运行级别3为例，init将执行配置文件inittab中的以下这行：<code>l5:5:wait:/etc/rc.d/rc 5</code>
- 这一行表示以5为参数运行/etc/rc.d/rc，/etc/rc.d/rc是一个Shell脚本，它接受5作为参数，去执行/etc/rc.d/rc5.d/目录下的所有的rc启动脚本，/etc/rc.d/rc5.d/目录中的这些启动脚本实际上都是一些连接文件，而不是真正的rc启动脚本，真正的rc启动脚本实际上都是放在/etc/rc.d/init.d/目录下。而这些rc启动脚本有着类似的用法，它们一般能接受start、stop、restart、status等参数。
- /etc/rc.d/rc5.d/中的rc启动脚本通常是K或S开头的连接文件，对于以以S开头的启动脚本，将以start参数来运行。而如果发现存在相应的脚本也存在K打头的连接，而且已经处于运行态了(以/var/lock/subsys/下的文件作为标志)，则将首先以stop为参数停止这些已经启动了的守护进程，然后再重新运行。这样做是为了保证是当init改变运行级别时，所有相关的守护进程都将重启。
- 至于在每个运行级中将运行哪些守护进程，用户可以通过chkconfig或setup中的"System Services"来自行设定。

#### 4. 建立终端
- rc执行完毕后，返回init。这时基本系统环境已经设置好了，各种守护进程也已经启动了。init接下来会打开6个终端，以便用户登录系统。在inittab中的以下6行就是定义了6个终端：

	```
	　　1:2345:respawn:/sbin/mingetty tty1
	　　2:2345:respawn:/sbin/mingetty tty2
	　　3:2345:respawn:/sbin/mingetty tty3
	　　4:2345:respawn:/sbin/mingetty tty4
	　　5:2345:respawn:/sbin/mingetty tty5
	　　6:2345:respawn:/sbin/mingetty tty6
	```
- 从上面可以看出在2、3、4、5的运行级别中都将以respawn方式运行mingetty程序，mingetty程序能打开终端、设置模式。同时它会显示一个文本登录界面，这个界面就是我们经常看到的登录界面，在这个登录界面中会提示用户输入用户名，而用户输入的用户将作为参数传给login程序来验证用户的身份。

#### 5. 用户登陆系统
- 对于运行级别为5的图形方式用户来说，他们的登录是通过一个图形化的登录界面。登录成功后可以直接进入KDE、Gnome等窗口管理器。而本文主要讲的还是文本方式登录的情况：当我们看到mingetty的登录界面时，我们就可以输入用户名和密码来登录系统了。
- Linux的账号验证程序是login，login会接收mingetty传来的用户名作为用户名参数。然后login会对用户名进行分析：如果用户名不是root，且存在/etc/nologin文件，login将输出nologin文件的内容，然后退出。这通常用来系统维护时防止非root用户登录。只有/etc/securetty中登记了的终端才允许root用户登录，如果不存在这个文件，则root可以在任何终端上登录。/etc/usertty文件用于对用户作出附加访问限制，如果不存在这个文件，则没有其他限制。
- 在分析完用户名后，login将搜索/etc/passwd以及/etc/shadow来验证密码以及设置账户的其它信息，比如：主目录是什么、使用何种shell。如果没有指定主目录，将默认为根目录；如果没有指定shell，将默认为/bin/bash。
- login程序成功后，会向对应的终端在输出最近一次登录的信息(在/var/log/lastlog中有记录)，并检查用户是否有新邮件(在/usr/spool/mail/的对应用户名目录下)。然后开始设置各种环境变量：对于bash来说，系统首先寻找/etc/profile脚本文件，并执行它；然后如果用户的主目录中存在.bash_profile文件，就执行它，在这些文件中又可能调用了其它配置文件，所有的配置文件执行后后，各种环境变量也设好了，这时会出现大家熟悉的命令行提示符，到此整个启动过程就结束了。 