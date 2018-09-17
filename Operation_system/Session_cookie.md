### Session管理和cookie 认证
 **我们网站通常使用的表单认证的，这个就是用户用用户名和密码进行登录。但是Http是无状态的协议，之前认证过的用户状态无法通过协议层保存下来，无法基于状管理。于是我们使用cookie来管理session，以弥补Http协议中存在的状态管理功能。**
```
 客户端                                                服务器
        1 发送登陆的账号信息    
        --------------------->      客户认证通过向客户发放Session ID， 记录登陆状态 (会把客户的认证状态和SessionID绑定后记录在服务器段)

        2 发送包含SessionID 的cookie set-Cookie:  
        <--------------------  
        3 发送Session ID 的cookie cokie:  
        --------------------->      通过判断Session来判断用户(客户端接收服务器段发来的SessionID 然后将其作为Cookie保存在本地。下次发送请求的时候浏览器自动发送Cookie 所以SessionID也同时发送到服务器，服务器段接收SessionID识别用户和认证状态)

```
