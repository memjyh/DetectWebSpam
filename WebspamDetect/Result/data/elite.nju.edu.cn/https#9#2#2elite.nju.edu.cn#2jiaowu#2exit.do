https://elite.nju.edu.cn/jiaowu/exit.do
<html>

	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		
		<title>南京大学教务系统</title>
		<link href="css/homepage.css" rel="stylesheet" type="text/css">

	</head>
	<script type="text/javascript">

	function CheckForm()
	{
		var ssValidateCode = "null";
		
		var oName = document.getElementById("userName");
		if(oName.value.length == 0)
		{
			alert("请输入用户名称!");
			oName.focus();
			return false;
		}
		
		var oPassword = document.getElementById("password");
		if(oPassword.value == "")
		{
			alert("请输入密码!");
			oPassword.focus();
			return false;
		}
		
		
		var oValidateCode = document.getElementById("ValidateCode");
		if(oValidateCode.value.length == 0)
		{
			alert("请输入验证码！");
			oValidateCode.focus();
			return false;
		}
		
		/*if(oName.value.length == 9 && (oName.value.substr(0,2) == '07' || oName.value.substr(0,2) == '08'))
		{
			oName.value = "";
			oPassword.value = ""
			oName.focus();
			return false;
		}*/
		
		// document.write("session:>" + ssValidateCode + "---img:>" + oValidateCode.value);
		return true;
	}
	
	function RefreshValidateImg(sValidateImgId)
	{
		document.getElementById(sValidateImgId).src = "ValidateCode.jsp?TimeCode=" + Math.random() + "100";
	}

</script>
	<body>
		<div id="Wrapper">
			<table width="740" height="100%" align="center" cellpadding="0" cellspacing="0">
				<tr>
					<td height="136">
						<div id="Logo">
							<a href="#"><img src="image/homepage/IndexLogo.jpg" border="0"> </a>
						</div>
					</td>
				</tr>
				<tr>
					<td height="39"></td>
				</tr>
				<tr>					
					<td height="341" id="Main">						    					
						<div id="Login">
						<font style="font-size: 12px;font-weight:bold;color: #FF0000"></font><br>
						<form method="post" action="login.do" onsubmit="JavaScript: return CheckForm();">
							<label>
								用户
							</label>
							<input id="userName" name="userName" type="text" class="InputBox Username">
							<br>
							<label>
								密码
							</label>
							<input type="password" id="password" name="password" class="InputBox Password">
							<input type="hidden" name="returnUrl" value="null">
							<br><br>
							
							<img style="margin-left:30px;" border="0" id="ValidateImg" src="ValidateCode.jsp">
							<a href="JavaScript:%20RefreshValidateImg('ValidateImg');">看不清？</a>
							<br>
							<label>
								验证
							</label>
							<input type="text" id="ValidateCode" name="ValidateCode" class="InputBox Username">
							<br>
							
							<input type="submit" class="Btn" value="" style="margin-left:30px;">
							<br>
							<br>
							<a target="_blank" href="help/index.htm" style="margin-left:30px;">使用帮助</a>
							<br>
							</form>
						</div>						
						<div id="News">							
							<ul>
								<label style="color: red;font-size: 12px;">教师登录：</label>
								<li>
									 用户名为工资号，初始密码为工资号，请及时更改密码。
								</li>
								<li>
									 可进入帮助了解如何使用本系统。
								</li>
								<br>
                                                                <label style="color: red;font-size: 12px;">新生登陆：</label>
								<li>
									 用户名为学号，初始密码为录取号的<strong>后6位</strong>（或学号）。
								</li>
								<br>
								<label style="color: red;font-size: 12px;">新生登录注意事项：</label>
								<li>
									 1. 请初次登录后进入【个人信息】核对您的基本信息。
								</li>
								<li>
									 2. 如果出生日期或身份证号有误请及时与辅导员联系。
								</li>
								<li>
									 3. 请填写个人联系方式，便于与您及时联系，谢谢。
								</li>
							</ul>
						</div>
					</td>					
				</tr>
				<tr>
					<td valign="top" id="Footer">
						Copyright © 2007 All Rights Reserved. 版权所有：南京大学教务处
						<a href="#">联系我们</a>
					</td>
				</tr>
			</table>
		</div>
	</body>
		
</html>