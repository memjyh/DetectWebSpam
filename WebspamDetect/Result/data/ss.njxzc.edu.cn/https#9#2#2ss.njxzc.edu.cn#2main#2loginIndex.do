https://ss.njxzc.edu.cn/main/loginIndex.do
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>南京晓庄学院智能办公系统</title>
    
<script type="text/javascript" src="/messages.do?__V=1542507535111"></script>
<script type="text/javascript" src="/js/utilities-241.js?__V=1414460794000"></script>
<script type="text/javascript" src="/js/ge.js?__V=1414460794000"></script>
<script type="text/javascript" src="/js/wiscom.js?__V=1414460794000"></script>
<script type="text/javascript" src="/js/ccs-min.js?__V=1414460794000"></script>
<script type="text/javascript" src="/oa/jquery-1.4.2.min.js?__V=1414460864000"></script>
<script type="text/javascript" src="/js/jsmodule/app-alertwindowpop.js?__V=1414460732000"></script>
    <script type="text/javascript">
        GE.cst.URL = "";
        GE.cst.URI = GE.cst.URL;
    </script>
    
    <style type="text/css">
        <!--
        body {
            background-image:url(/themes/wisedu_oa_lovey/basic/images/login_body_bg1.jpg);
            background-position:top center;
            background-repeat:repeat-x;
            background-color:#edf7f9;
            margin:0;
            padding:0;
            color:#333333;
            font-size:12px;
            line-height:24px;
            text-align:left;
        }
        .logintitle {
            font-size:24px;
            font-family:"微软雅黑";
            color:#005973;
            font-weight:100;
        }
        .foot_text {
            font-size:12px;
            font-family:"微软雅黑";
            color:#999999;
        }
        .STYLE2 {font-size: 21px; font-family: "微软雅黑"; color: #005973; font-weight: 100; }
        -->
    </style>

    <script type="text/javascript">
        function loginsubmit(){
            $('#loginform').submit();
        }


        function keydownPass(evt){
            evt = (evt) ? evt : ((window.event) ? window.event : "")
            keyCode = evt.keyCode ? evt.keyCode : (evt.which ? evt.which: evt.charCode);
            if (keyCode == 13) {
                loginsubmit();
            }
        }
    </script>
</head>

<body>
<form id="loginform" method="post" action="/main.login.do?invitationCode=">
    <table width="100%" height="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td><table style="width:1002px; height:568px;text-align:left;" border="0" align="center" cellpadding="0" cellspacing="0">
                <tr>
                    <td valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">

                        <tr>
                            <td width="97%" height="100" valign="bottom"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td><img src="/themes/wisedu_oa_lovey/basic/images/logo2.png"></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td height="400" style="padding-left:10px;"><table width="97%" border="0" align="left" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td align="right"><table width="300" height="220" border="0" cellpadding="0" cellspacing="0">
                                        <tr>
                                            <td height="70" colspan="2" valign="middle"><img src="/themes/wisedu_oa_lovey/basic/images/ico.png" width="38" height="44" align="absmiddle">  <span class="STYLE2">用户登录</span></td>
                                        </tr>
                                        <tr>
                                            <td height="22" colspan="2"> </td>
                                        </tr>
                                        <tr>
                                            <td width="78" align="left" valign="middle"><img src="/themes/wisedu_oa_lovey/basic/images/name.jpg" width="78" height="30"></td>
                                            <td width="322" align="left" valign="middle"><input name="email" id="email" type="text" style="height:30px; line-height:24px; width:200px;"></td>
                                        </tr>
                                        <tr>
                                            <td height="20" colspan="2"> </td>
                                        </tr>
                                        <tr>
                                            <td width="78"><img src="/themes/wisedu_oa_lovey/basic/images/password.jpg" width="78" height="30"></td>
                                            <td width="322"><input type="password" name="password" id="password" style="height:30px; line-height:24px; width:200px;" onkeydown="keydownPass(event)"></td>
                                        </tr>
                                        <tr>
                                            <td height="30" colspan="2"> </td>
                                        </tr>
                                        <tr>
                                            <td colspan="2"><div align="center"><img src="/themes/wisedu_oa_lovey/basic/images/enter.jpg" alt="login" width="144" height="30" onclick="loginsubmit()"></div></td>
                                        </tr>
                                        <tr>
                                            <td height="22" colspan="2" style="padding-left:107px;">
                                                
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height="20" colspan="2"> </td>
                                        </tr>
                                    </table></td>
                                    <td align="center"><img src="/themes/wisedu_oa_lovey/basic/images/pics.png" width="616px"></td>
                                </tr>
                            </table></td>
                        </tr>
                        <tr>
                            <td height="50" align="center" class="foot_text">Copyright 2014 南京晓庄学院 All rights reserved</td>
                        </tr>
                    </table></td>
                </tr>

            </table></td>
        </tr>
    </table>
</form>
</body>
</html>