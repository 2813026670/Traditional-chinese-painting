使用方法：
	准备：
		安装VUE及其脚手架工具
		安装VScode
		部署太乙模型：https://divis.yuque.com/ofu7m9/rfbv7m/bg9burfrs46vga1p
	使用：
		启动项目，输入npm run dev(将看到浏览器中的http://localhost:5173/页面)
		启动main_server.py，输入python main_server.py(将看到Loading pipeline components...开头的加载条)
		图像生成：在浏览器页面中选择国画相关的提示词，点击生成图片按钮，画作概览模块中会显示生成的图片，推荐调色板模块中显示相应的配色方案

前端：使用VUE
	分为四部分：控制面板、画作概览、推荐调色板、测试调色板
		控制面板包括：反馈框、下拉选择框、单选框、生成图片按钮
			反馈框：显示通过下拉选择框选择的选项。
			下拉选择框：用于选择具有国画背景知识的提示词,包括主题,意境,物象,技法,赋彩方式。		
			单选框：用于指定国画五色系 (青赤黄白黑)或单色配色方案。
			生成图片按钮：提示词将输入微调后的太乙模型以生成图像。
		画作概览：预览生成图像。
		推荐调色板：配色方案以色块形式直观展示,用户能够通过下拉选框选择查看颜色对应的国画色彩名称或 RGB 值。
		测试调色板：可以上传任意灰度图像, 然后使用 推荐调色板 模块中选择的配色方案对图像上色

后端：使用FLASK