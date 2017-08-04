### ColorMatchApi

BaseUrl: http://api.wjmwjmwb.com #线上环境

BaseDevUrl: http://dev.wjmwjmwb.com #开发环境(暂时未启用)

[通过图片URL获取图片配色方案](#通过图片URL获取图片配色方案)

[获取七牛上传token](#获取七牛上传token)

<a name = "通过图片URL获取图片配色方案">

####  通过图片URL获取图片配色方案 

URL：/color

Method: Post

Params:

* image_url	#图片网址

Return: 

```json
{
    "code": 200, #状态码 200正确 501是错误码
    "dominant": {#主色调
        "B": 115,
        "G": 201,
        "R": 0
    },
    "palette": [#8个颜色		percentage:该颜色所占百分比
        {
            "RGB": {
                "B": 115,
                "G": 201,
                "R": 0
            },
            "percentage": 0.71,
            "hex":"#2da4ff"
        },
        {
            "RGB": {
                "B": 46,
                "G": 46,
                "R": 44
            },
            "percentage": 0.09,
            "hex":"#2da4ff"
        },
        ....
    ]
}
```

<a name = "获取七牛上传token">

####  获取七牛上传token 

URL：/uploadtoken

Method: Get

Params: nil

Return: 

```json
{
    "code": 200, #状态码 200正确 501是错误码
    "token": "271mDStmwp900AFRIvQ8S6d-y:RIV9LXGILHPRyIC1Mb6nfMIXInQ=:eyJzY29wZSI6InBob3RvIi"
}