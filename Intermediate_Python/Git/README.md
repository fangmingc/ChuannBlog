## git

### 操作命令
#### git add
- 添加版本追踪：git add [文件名]
- 追踪所有变化：git add .

#### git commit
- 确认提交：git commit -m "提交说明"

#### git checkout
- 切换分支： git checkout [分支名]

#### git merge
- 合并分支： git merge [分支名]

#### git branch
- 查看分支：git branch  
- 删除分支：git branch -d [分支名]
- 强制删除分支：git branch -D [分支名]
#### git pull
- 同步远端到本地:git pull

#### git push
- 提交本地更改到远端:git push

#### git reset
- 回退上一个版本：git reset --hard HEAD^  
- 回退指定版本：git reset --hard [版本号]

#### git revert
- 删除最近一次提交：git revert HEAD

#### git log
- 查看版本日志：git log


### 回退远端仓库
#### 方法一
适用次数少的回退  
第一步：删除最后一次提交  
git revert HEAD  
第二步：提交更改
git push origin master   
#### 方法二
慎重！慎重！慎重！  
务必在所有提交者都确认的情况使用本方法！！   
第一步：回退到指定版本  
git reset --hard HEAD[回退的版本号]   
第二步：强制提交更改   
git push origin master -f   


