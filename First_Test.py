#encoding=utf-8
import unittest
from selenium import webdriver
import time
from login import login
from com.study import article



class First_Test(unittest.TestCase):
    dr = None    
    all_article_url = "http://localhost/wordpress/wp-admin/edit.php"
    write_article_url = "http://localhost/wordpress/wp-admin/post-new.php"

    def setUp(self):
        self.dr = webdriver.Chrome()
        print 'setUp'
        
        
    def test_class_one(self):   
        #登陆  
        login(self.dr)        
        print self.dr.current_url      
        self.assertTrue("wp-admin" in self.dr.current_url)
        
        
        #写文章        
        self.dr.get(self.write_article_url)
        title = article.write_article(self.dr)
        self.dr.get(self.all_article_url)
        table = self.dr.find_element_by_class_name("wp-list-table")
        #验证新添加的文章标题在表格内
        self.assertTrue(title in table.text)
        
        #删除新增加的文章
        time.sleep(3)        
        article.delete_article(self.dr,title)
        #重新获取table的text
        table = self.dr.find_element_by_class_name("wp-list-table")
        self.assertFalse(title in table.text)
        
        #所有文章界面写文章            
        title = article.add_write_article(self.dr)
        self.dr.get(self.all_article_url)
        table = self.dr.find_element_by_class_name("wp-list-table")
        #验证新添加的文章标题在表格内
        self.assertTrue(title in table.text)
        
        
        #编辑文章        
        title = article.edit_article(self.dr,title)
        self.dr.get(self.all_article_url)
        table = self.dr.find_element_by_class_name("wp-list-table")
        #验证新添加的文章标题在表格内
        self.assertTrue(title in table.text)
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
    def tearDown(self):
        time.sleep(3)
        print 'close page'
        self.dr.quit()
    
if __name__=="__main__":
    unittest.main()
