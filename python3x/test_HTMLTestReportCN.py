# -*- coding:utf-8 -*-

import unittest
import HTMLTestReportCN



#测试用例

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.case_id = ''
        self.case_descript = ''

    def tearDown(self):
        pass


    def testCase1(self):
        self.case_id = 'test_pass_001'
        self.case_descript = '测试成功的样式'
        self.assertEqual(2,2,"testSucess")


    def testCase2(self):
        self.case_id = 'test_fail_002'
        self.case_descript = '测试失败的样式'
        self.assertEqual(2,3,"testFail")

    def testCase3(self):
        self.case_id = 'test_fail_003'
        self.case_descript = '测试失败的样式'
        self.assertEqual(2,5,"测试失败")

    def testCase4(self):
        self.case_id = 'test_fail_004'
        self.case_descript = '测试失败的样式'
        self.assertEqual(2,1,"测试失败")

    def testCase5(self):
        pass

class APITestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase1(self):
        self.case_id = 'test_pass_001'
        self.case_descript = '测试成功的样式'
        self.assertEqual(2, 2, "testPass")

    def testCase2(self):
        self.case_id = 'test_pass_002'
        self.case_descript = '测试成功的样式'
        self.assertEqual(3, 3, "testPass")

    def testCase3(self):
        self.case_id = 'test_pass_003'
        self.case_descript = '测试成功的样式'
        self.assertEqual(5, 5, "testPass")

    def testCase4(self):
        self.case_id = 'test_fail_004'
        self.case_descript = '测试失败的样式'
        self.assertEqual(2, 1, "测试错误")

    def testCase5(self):
        self.case_id = 'test_fail_005'
        self.case_descript = '测试失败的样式'
        self.assertEqual(2, 9, "testFail")

    def testCase6(self):
        self.case_id = 'test_pass_006'
        self.case_descript = '测试成功的样式'
        pass
    def testCase7(self):
        self.case_id = 'test_error_007'
        self.case_descript = '测试错误的样式'
        a==b

#添加Suite
def Suite():
    #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    #将测试用例加入到容器
    suiteTest.addTest(MyTestCase("testCase1"))
    suiteTest.addTest(MyTestCase("testCase2"))
    suiteTest.addTest(MyTestCase("testCase3"))
    suiteTest.addTest(MyTestCase("testCase4"))
    suiteTest.addTest(MyTestCase("testCase5"))
    suiteTest.addTest(APITestCase("testCase1"))
    suiteTest.addTest(APITestCase("testCase2"))
    suiteTest.addTest(APITestCase("testCase3"))
    suiteTest.addTest(APITestCase("testCase4"))
    suiteTest.addTest(APITestCase("testCase5"))
    suiteTest.addTest(APITestCase("testCase6"))
    suiteTest.addTest(APITestCase("testCase7"))
    return suiteTest

'''
问题：代码写的没问题，执行也成功了，但就是无法生成HTMLTestRunner的报告
其实这是编辑器搞得鬼，编辑器为了方便用户执行测试，都有一项功能，可以用编辑器来调用unittest或者nose来执行测试用例，这种情况下，执行的只是用例或者套件，而不是整个文件，写在main里的代码是不会被执行的！！自然无法生成测试报告
我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行
if __name__ == ‘__main__‘:
if __name__ == ‘python‘:
# 把main修改成自己的文件夹名就可以了

---试了不行
'''
if __name__ == '__main__':
    import os
    print(os.getcwd())
    #确定生成报告的路径
    filePath ='HTMLTestReportCN.html'
    fp = open(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        #description='详细测试用例结果',
        tester='Sycing'
        )
    #运行测试用例
    runner.run(Suite())
    # 关闭文件，否则会无法生成文件
    #fp.close()