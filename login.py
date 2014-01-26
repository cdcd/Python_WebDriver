
login_url = "http://localhost/wordpress/wp-login.php"
def login(dr):    
    dr.get(login_url)
    dr.find_element_by_name("log").send_keys('admin')
    dr.find_element_by_name("pwd").send_keys('admin')
    dr.find_element_by_name("wp-submit").click()