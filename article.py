#encoding=utf-8
import time
from selenium import webdriver


all_article_url = "http://localhost/wordpress/wp-admin/edit.php"
    
def write_article(dr):    
    content = "new post" +str(time.time())
    dr.find_element_by_name('post_title').send_keys(content)
    js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" +content+"'"
    print js
    dr.execute_script(js)
    dr.find_element_by_name('publish').click()
    return content
    
def delete_article(dr,title):
    dr.get(all_article_url)
    webdriver.ActionChains(dr).move_to_element(dr.find_element_by_xpath("//a[text()='"+title+"']")).perform()
    dr.find_element_by_xpath("//a[text()='"+title+"']/ancestor::td[1]//a[text()='移至回收站']").click()
    
def add_write_article(dr):
    dr.get(all_article_url)
    dr.find_element_by_class_name("add-new-h2").click()
    return write_article(dr)
    
def edit_article(dr,title):
    dr.get(all_article_url)
    webdriver.ActionChains(dr).move_to_element(dr.find_element_by_xpath("//a[text()='"+title+"']")).perform()
    dr.find_element_by_xpath("//a[text()='"+title+"']/ancestor::td[1]//a[text()='编辑']").click() 
    
    #修改文章内容
    content = "eidt post__" +str(time.time())
    dr.find_element_by_name('post_title').clear()
    dr.find_element_by_name('post_title').send_keys(content)
    js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" +content+"'"
    print js
    dr.execute_script(js)
    dr.find_element_by_id('publish').click()
    return content
