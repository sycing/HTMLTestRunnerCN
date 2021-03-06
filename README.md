[说明]
=========================
HTMLTestRunner输出的报告真的很丑,于是找了一圈没有我自已想要的html，所以自己动手进行了美化<br>
原作者文件下载地址：http://tungwaiyip.info/software/HTMLTestRunner.html<br>
我基于其Version 0.8.2进行了修改美化具体内容如下：<br>
```python

Version 0.8.2.3 -Sycing
*仅修改py3中文部分
   # Version 0.8.2.3
   #增加错误结果的按钮
   #增加用例编号，用例描述两列
   #错误用例显示为橘黄色
   #总计列移动到错误后面
   #概要按钮去掉通过率显示
   #测试脚本的测试用例必须增加：self.case_id,self_descript

Version 20170609   -Findyou
* python3x  #仅支持python3x
   # Version 0.8.2.2
   # HTMLTestReportCN.py  中文报告
   # HTMLTestReportEN.py  英文报告
   
* python2x  #仅支持python2x
   # Version 0.8.2.1
   # HTMLTestRunnerEN.py  中文报告
   # HTMLTestRunnerCN.py  英文报告


Version 0.8.2.1 -Findyou
* CN汉化，EN保留英文，加Utf-8支持报告中文字符
* 增加 样式美化（需要网络）
* 增加 通过用例 分类按钮
* 增加 测试人员显示、通过率的统计
* 增加 按钮显示相应用例数
* 修改 测试结果的展示，方便拷贝数据
* 修改“详细”逻辑，增加与“收起”效果变换
* 右侧底部增加 返回 顶部的锚点
```
[如何使用]
=========================
一、HTMLTestRunnerEN（python2.x） 使用
--------------------------
有时大伙会觉得英语会有莫名的逼格（感叹,沉默），所以保留了英文显示，满足大家的需要，报告内容支持中文显示。
<br>
* 编写test_HTMLTestRunnerEN.py<br>
```python
import HTMLTestRunnerEN
...

if __name__ == '__main__':
    filePath ='F:\\Report.html'
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerEN.HTMLTestRunner(
        stream=fp,
        title='{ Test Report }',
        #description='',
        #tester="Findyou"
        )
    runner.run(Suite())
```

* 执行test_HTMLTestRunnerEN.py<br>
```python
python test_HTMLTestRunnerEN.py
```

* 执行结果：Report.html
![](https://github.com/findyou/python/blob/master/Report_EN.gif "测试结果") 


二、HTMLTestRunnerCN（python2.x） 使用
--------------------------
使用同HTMLTestRunnerEN，无区别<br>
* 执行结果：Report.html
![](https://github.com/sycing/HTMLTestRunnerCN/blob/master/Report_CN.gif "测试结果") 



三、`HTMLTestReportCN（python3.x） 使用`
--------------------------
使用HTMLTestRunnerCN，测试用例中必须增加 `self.case_id、self.case_descript`<br>
* 编写test_HTMLTestRunnerCN.py<br>
```python
import HTMLTestRunnerEN
...
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase1(self):
        self.case_id = 'test_pass_001'#必须增加
        self.case_descript = '测试成功的样式'#必须增加
        self.assertEqual(2,2,"testSucess")

if __name__ == '__main__':
    filePath ='F:\\Report.html'
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerEN.HTMLTestRunner(
        stream=fp,
        title='{ Test Report }',
        #description='',
        #tester="Findyou"
        )
    runner.run(Suite())
```

* 执行test_HTMLTestRunnerEN.py<br>
```python
python test_HTMLTestRunnerEN.py
```
* python3.x 中文执行结果：Report.html
![](https://github.com/sycing/HTMLTestRunnerCN/blob/master/Report_CN_py3.gif "测试结果") 

四、HTMLTestReportEN（python3.x） 使用
--------------------------
使用同HTMLTestRunnerEN，无区别<br>
 <br>
