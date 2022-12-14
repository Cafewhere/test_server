import json

def getTest():
    var = {
        "version": "2.0",
        "template": {
            "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                    "title": "보물상자",
                    "description": "보물상자 안에는 뭐가 있을까",
                    "thumbnail": {
                        "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                    },
                    "buttons": [
                        {
                        "action": "message",
                        "label": "열어보기",
                        "messageText": "짜잔! 우리가 찾던 보물입니다"
                        },
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                        }
                    ]
                    },
                    {
                    "title": "보물상자2",
                    "description": "보물상자2 안에는 뭐가 있을까",
                    "thumbnail": {
                        "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                    },
                    "buttons": [
                        {
                        "action": "message",
                        "label": "열어보기",
                        "messageText": "짜잔! 우리가 찾던 보물입니다"
                        },
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                        }
                    ]
                    },
                    {
                    "title": "보물상자3",
                    "description": "보물상자3 안에는 뭐가 있을까",
                    "thumbnail": {
                        "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                    },
                    "buttons": [
                        {
                        "action": "message",
                        "label": "열어보기",
                        "messageText": "짜잔! 우리가 찾던 보물입니다"
                        },
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                        }
                    ]
                    }
                ]
                }
            }
            ]
        }
    }

    jsonString = json.dumps(var)

    return jsonString