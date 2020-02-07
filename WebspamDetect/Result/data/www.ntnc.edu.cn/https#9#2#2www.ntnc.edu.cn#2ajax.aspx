https://www.ntnc.edu.cn/ajax.aspx
<html>
    <head>
    <style type="text/css">
		BODY { color: #000000; background-color: white; font-family: Verdana; margin-left: 0px; margin-top: 0px; }
		#content {font-size:12px; margin-left: 30px; padding-bottom: 2em; }
		A:link { color: #336699; font-weight: bold; text-decoration: underline; }
		A:visited { color: #6699cc; font-weight: bold; text-decoration: underline; }
		A:active { color: #336699; font-weight: bold; text-decoration: underline; }
		A:hover { color: cc3300; font-weight: bold; text-decoration: underline; }
		P { color: #000000; margin-top: 0px; margin-bottom: 12px; font-family: Verdana; }
		pre { background-color: #e5e5cc; padding: 5px; font-family: Courier New; border: 1px #f0f0e0 solid; }
		td { color: #000000; font-family: Verdana; font-size: .7em; }
		h2 { font-size: 1.5em; font-weight: bold; margin-top: 25px; margin-bottom: 10px; border-top: 1px solid #003366; margin-left: -15px; color: #003366; }
		h3 { font-size: 1.1em; color: #000000; margin-left: -15px; margin-top: 10px; margin-bottom: 10px; }
		ul { margin-top: 10px; margin-left: 20px; }
		ol { margin-top: 10px; margin-left: 20px; }
		li { margin-top: 10px; color: #000000; }
		font.value { color: darkblue; font: bold; }
		font.key { color: darkgreen; font: bold; }
		font.error { color: darkred; font: bold; }
		.heading1 { color: #ffffff; font-family: Tahoma; font-size: 26px; font-weight: normal; background-color: #003366; margin-top: 0px; margin-bottom: 0px; margin-left: -30px; padding-top: 10px; padding-bottom: 3px; padding-left: 15px; width: 105%; }
		.button { background-color: #dcdcdc; font-family: Verdana; font-size: 1em; border-top: #cccccc 1px solid; border-bottom: #666666 1px solid; border-left: #cccccc 1px solid; border-right: #666666 1px solid; }
		.frmheader { color: #000000; background: #dcdcdc; font-family: Verdana; font-size: .7em; font-weight: normal; border-bottom: 1px solid #dcdcdc; padding-top: 2px; padding-bottom: 2px; }
		.frmtext { font-family: Verdana; font-size: .7em; margin-top: 8px; margin-bottom: 0px; margin-left: 32px; }
		.frmInput { font-family: Verdana; font-size: 1em; }
		.intro { margin-left: -15px; }
           
</style>
<title>Ajax Web 服务</title>
</head>
<body>
<div id="content">
<p class="heading1">Ajax</p><br>
<span>
    <p class="intro">调用本服务，需要在页面中加入JS引用<br><br>
</p><pre><b>&lt;script language="javascript" type="text/javascript" src="{PE.SiteConfig.installdir /}JS/Common.js"&gt;&lt;/script&gt;</b>
</pre>
<br>
    本AJAX服务，支持下列操作。有关正式定义，请查看<a href="http://help.powereasy.net/pe2007/ajaxservices">服务说明</a>。 
    <ul>
    <li>
    用户验证
    <span>
    <br>检验用户是否存在,如存在则返回false，页面内需有ID为username 这个输入框。<br><br>
<pre>
&lt;span onclick="usercheck('输出检测结果元素ID')"&gt;点击检查用户名&lt;/span&gt;
</pre>
    </span>
    </li>
    <p>
    </p><li>
    用户登录
    <span>
    <br>用户登录过程,页面内须有ID为username, password, checkcode 这三个输入框。<br><br>
<pre>
&lt;span onclick="userlogin()"&gt;登录&lt;/span&gt;
</pre>
    </span>
    </li>
    <p>
    </p><li>
    更新标签内容
    <span>
    <br>AJAX方式更新标签内容，一般用于分页等。<br><br>
<pre>
function changepage(spanname,sourcename,pagenum)
{
	var x = new AjaxRequest('XML','pe100_' + sourcename);
        x.labelname = sourcename;
        x.pagename = "当前页面名，特殊情况用，AJAX调用时可不填";
        x.currentpage = pagenum;
	    x.para = [标签参数列表，请使用二维字符阵列形式填写];
	    x.post('updatelabel', 'ajax.aspx', function(s) {
            var xml = x.createXmlDom(s);
            $("pe100_" + sourcename).innerHTML = xml.getElementsByTagName("body")[0].firstChild.data;

            updatepage(spanname, sourcename, xml); /* 如需要更新分页列表，则需要本行 */
	 });
}
</pre>
    </span>
    </li>
    <p>
    </p><li>
    更新分页标签内容
    <span>
    <br>AJAX方式更新分页标签,一般配合上面的AJAX标签更新使用。<br><br>
<pre>
function updatepage(spanname, sourcename, xml)
{
	var x = new AjaxRequest('XML','pe100_page_' + sourcename);
         x.labelname = spanname;
        x.sourcename = sourcename;
        x.total = xml.getElementsByTagName("total")[0].firstChild.data;
        x.currentpage = xml.getElementsByTagName("currentpage")[0].firstChild.data;
        x.pagesize = xml.getElementsByTagName("pagesize")[0].firstChild.data;
	    x.post('updatepage', 'ajax.aspx', function(s) {
            var xml = x.createXmlDom(s);
            $("pe100_page_" + sourcename).innerHTML = xml.getElementsByTagName("body")[0].firstChild.data;
	 });
}
</pre>
    </span>
    </li>
    <p>
    </p><li>
    发表评论
    <span>
    <br>发表评论，页面内需有ID为username,content,face,email,gid,nid,tid,private,position,score,ip 这七个输入框。<br><br>
<pre>
&lt;span onclick="addcommon()"&gt;发表&lt;/span&gt;
</pre>
    </span>
    </li>
    <p>
    </p><li>
    获取系统固定标签内容
    <span>
    <br>获取系统中固定标签的内容, 参数说明：labelname 调用标签名, targetid AJAX状态输出，为空则不显示。<br>
<pre>
function getlabel(labelname, targetid)
{
	var x = new AjaxRequest('XML',targetid);
        x.post(labelname, 'ajax.aspx', function(s) {
            var xml = x.createXmlDom(s);
            $(targetid).innerHTML = xml.getElementsByTagName("body")[0].firstChild.data;
	 });
}
</pre>
    </span>
    </li>
    </ul>
</span>
<span>
<hr>
   <h3>使用中如有任何疑问，请联系动易公司售后服务部门。</h3>
</span>    
</div></body>
</html>