import json
from app.models import Game

# A string containing JSON data

json_string = '''[
    {
        "name": "Stardew Valley",
        "image": "https://image.api.playstation.com/cdn/UP2456/CUSA06840_00/0WuZecPtRr7aEsQPv2nJqiPa2ZvDOpYm.png",
        "platforms": [
            "PC",
            "Mobile",
            "Playstation"
        ],
        "screenshots": [
            "https://www.researchgate.net/publication/319360746/figure/fig4/AS:617221277634561@1524168428758/A-screenshot-from-Stardew-Valley-showing-the-players-farm-inventory-and-avatar.png",
            "https://images.nintendolife.com/a2963e721d151/stardew-valley.large.jpg",
            "https://www.rpgfan.com/wp-content/uploads/2020/07/Stardew-Valley-Screenshot-026.jpg",
            "https://steamuserimages-a.akamaihd.net/ugc/948470786126242250/7E7B886EA551FE4EABBA741DD7A15B00CD71B379/?imw=1024&imh=640&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true",
            "https://steamuserimages-a.akamaihd.net/ugc/809930675825831119/D6638073FFE9C134412BF1CD2CC4EBFCF06A75AB/?imw=1024&imh=576&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true",
            "https://www.newgamenetwork.com/images/uploads/gallery/StardewValley/sv_06.jpg",
            "https://steamuserimages-a.akamaihd.net/ugc/262717050090984483/0E71852B8FC58F34A3F49DA638626CAAA809E1C3/?imw=1024&imh=576&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true"
        ]
    },
    {
        "name": "Stray",
        "image": "https://image.api.playstation.com/vulcan/ap/rnd/202206/0300/E2vZwVaDJbhLZpJo7Q10IyYo.png",
        "platforms": [
            "PC",
            "Xbox",
            "Playstation"
        ],
        "screenshots": [
            "https://www.adrenaline.com.br/wp-content/uploads/2022/07/stray-2.jpg",
            "https://m.media-amazon.com/images/I/713pP+GRv+L._AC_UF1000,1000_QL80_.jpg",
            "https://cdn.akamai.steamstatic.com/steam/apps/1332010/ss_a697971e484b3deef50153a13f2afd0539347d23.1920x1080.jpg?t=1709318461",
            "https://cdn.akamai.steamstatic.com/steam/apps/1332010/ss_e8f0cbd5efdba352e89c4cfcee3fe991a1e1be8a.1920x1080.jpg?t=1709318461",
            "https://oyster.ignimgs.com/mediawiki/apis.ign.com/stray/2/27/Stray2-3.jpg?width=1280",
            "https://sm.ign.com/ign_br/feature/s/stray-10-t/stray-10-totally-normal-cat-things-you-can-do_c477.jpg",
            "https://www.adrenaline.com.br/wp-content/uploads/2022/07/stray-numeros-steam_3.jpg"
        ]
    },
    {
        "name": "Hollow Knight",
        "image": "https://image.api.playstation.com/cdn/UP1822/CUSA13632_00/GuFQKWlrIVODEA1su20fCOrNZEYX5CB9.png",
        "platforms": [
            "PC",
            "Xbox",
            "Playstation",
            "Nintendo Switch"
        ],
        "screenshots": [
            "https://cdn.akamai.steamstatic.com/steam/apps/367520/ss_d5b6edd94e77ba6db31c44d8a3c09d807ab27751.1920x1080.jpg?t=1695270428",
            "https://cdn.akamai.steamstatic.com/steam/apps/367520/ss_2329fe632e788efd9ece9dcfc98c0ea723ac0d04.1920x1080.jpg?t=1695270428",
            "https://m.media-amazon.com/images/M/MV5BMDViZWFhYmYtODU4Yi00YTQ3LWI3YjctNzExYjY5Y2NmYzRkXkEyXkFqcGdeQXVyNjc3OTE4Nzk@._V1_.jpg",
            "https://m.media-amazon.com/images/M/MV5BZDI2ZDcyYzktMDA3NC00NDIzLTgwZGEtNzg4M2Y1MjYyMjkzXkEyXkFqcGdeQXVyNjc3OTE4Nzk@._V1_.jpg",
            "https://m.media-amazon.com/images/M/MV5BMDgyNTk2M2ItZDE1OS00Y2E5LTk2NjctODY4NmZiYTFhMDQxXkEyXkFqcGdeQXVyNjc3OTE4Nzk@._V1_.jpg",
            "https://i.pinimg.com/originals/88/19/be/8819bed1dc24834ce216cf4a1c96f9f7.jpg",
            "https://static.wikia.nocookie.net/hollowknight/images/0/0d/Gameplay_Demonstration_-_Brooding_Mawlek/revision/latest/scale-to-width-down/250?cb=20170413210505"
        ]
    },
    {
        "name": "Hades",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBsHntpflUqmx87FXSS1LQqw4Fk92Lt2S6sNa0uJP9eQ&s",
        "platforms": [
            "PC",
            "Xbox",
            "Playstation",
            "Nintendo Switch"
        ],
        "screenshots": [
            "https://images.ctfassets.net/wn7ipiv99ue5v/4SThOnxXgMEKY0ibxFyrxX/4e4b363402c5a71d1e031514a01cfd6e/Hades_4K_CoolTonesEnvironment.jpg",
            "https://m.media-amazon.com/images/I/818hLxkQudS.jpg",
            "https://m.media-amazon.com/images/I/81EK+z8BuoS.jpg",
            "https://cdn.akamai.steamstatic.com/steam/apps/1145360/ss_bcb499a0dd001f4101823f99ec5094d2872ba6ee.1920x1080.jpg?t=1702510146",
            "https://cdn.akamai.steamstatic.com/steam/apps/1145360/ss_abb2427810a4e91cc600f37c3630b912d4e0191b.1920x1080.jpg?t=1702510146",
            "https://cdn.akamai.steamstatic.com/steam/apps/1145360/ss_5e52844b891b54608eb51a850d6b53313eeed0f7.1920x1080.jpg?t=1702510146",
            "https://cdn.akamai.steamstatic.com/steam/apps/1145360/ss_68300459a8c3daacb2ec687adcdbf4442fcc4f47.1920x1080.jpg?t=1702510146"
        ]
    },
    {
        "name": "Outer Wilds",
        "image": "https://image.api.playstation.com/vulcan/ap/rnd/202208/1623/Zofebh60Ue7Zt5sC10UAtU3D.png",
        "platforms": [
            "PC",
            "Xbox",
            "Playstation",
            "Nintendo Switch"
        ],
        "screenshots": [
            "https://tm.ibxk.com.br/2024/03/15/15111816429100.jpg?ims=352x208",
            "https://assets.nintendo.com/image/upload/ar_16:9,b_auto:border,c_lpad/b_white/f_auto/q_auto/dpr_2.0/c_scale,w_400/ncom/software/switch/70010000038712/5b41cee1871ab7a0541e72dcd41a2c1f84ef0e3b03bdcb330552592a6f0ac2a7",
            "https://oyster.ignimgs.com/mediawiki/apis.ign.com/outer-wilds/a/ad/Owilds_reservoir_1.jpg",
            "https://cdn.vox-cdn.com/thumbor/nPT9ZghgMMaG0hyNLhhUJbXuZBs=/0x0:1920x1080/1200x800/filters:focal(807x387:1113x693)/cdn.vox-cdn.com/uploads/chorus_image/image/64769392/Outer_Wilds_beginner_s_guide_cover.0.png",
            "https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/QNXL4ZKOC5ET5FA6TJY23LWTNI.jpg",
            "https://assets1.ignimgs.com/thumbs/userUploaded/2019/5/30/36190303outerwildsblogroll-1559251761938.jpg",
            "https://imgcdn.agendadigitale.eu/wp-content/uploads/2020/11/14161354/outer-wilds.jpg"
        ]
    },
    {
        "name": "GRIS",
        "image": "https://image.api.playstation.com/vulcan/ap/rnd/202211/1801/PMjvy3y1p6gkPsBwCUuaFnfv.jpg",
        "platforms": [
            "PC",
            "Xbox",
            "Playstation",
            "Nintendo Switch",
            "Mobile"
        ],
        "screenshots": [
            "https://s2-techtudo.glbimg.com/NgS6Cgwb5NxO9RKaXZNCdaLzN08=/0x0:1920x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2023/U/P/wkv4moTKOrOXBzGEWjNQ/imagem-2023-09-05-215448239.png",
            "https://cdn.akamai.steamstatic.com/steam/apps/683320/ss_62883bfa8a341db3f9c5c03768f5c14f938fe8fc.1920x1080.jpg?t=1710929923",
            "https://cdn.vox-cdn.com/thumbor/FTGflhW34E25BS2EQcrCVE6U_Sk=/0x0:1920x1080/1200x675/filters:focal(1019x358:1325x664)/cdn.vox-cdn.com/uploads/chorus_image/image/62668832/ss_631d99cc6462cce94081032b7e600a6b87c3f7d3.0.jpg",
            "https://image.api.playstation.com/vulcan/img/cfn/11307gHAhRchUMjM4ZfOtl8y0brSJgvikLvCTm7QVOZxd5cojIj1XSWlnSqP7g-w02lCRlzg68ZW3FBcQSOfaOX9WvAnr5Kl.jpg",
            "https://assets.nuuvem.com/image/upload/t_screenshot_full/v1/products/5c8677a08810245e063b4c66/screenshots/zt1nc1q5uscmyefco1pt.jpg",
            "https://play-lh.googleusercontent.com/lp0mkH-R3vDOlBgpfDEuDyzwMFX0PbUJHk5UsYmlZVgMRfXvrE28q0DW3fLj8yURY0o",
            "https://the-artifice.com/wp-content/uploads/2020/04/Gris-Movement-and-Controls.jpeg"
        ]
    },
    {
        "name": "Overcooked 2",
        "image": "https://cdn1.epicgames.com/salesEvent/salesEvent/egs-overcooked2-tall_1200x1600-fbae89fad70c05cd1979316f620e64a9",
        "platforms": [
            "PC",
            "Xbox",
            "Playstation",
            "Nintendo Switch"
        ],
        "screenshots": [
            "https://store-images.s-microsoft.com/image/apps.29751.14184096619580431.90f674bc-0c36-4602-85d7-e95340e27b11.d4386aef-81cf-41d7-948f-d1d7329fdcb2?q=90&w=320&h=180",
            "https://m.media-amazon.com/images/I/81tyhGj9ZRL._AC_UF350,350_QL80_.jpg",
            "https://cdn.akamai.steamstatic.com/steam/apps/1138400/ss_9b5e61b57c6624a70ba827346de239fe103f2362.1920x1080.jpg?t=1580470362",
            "https://cdn.akamai.steamstatic.com/steam/apps/1138400/ss_16d2306bd0217879459df9f801d1f32460681f9c.1920x1080.jpg?t=1580470362",
            "https://assets.nintendo.com/image/upload/ar_16:9,b_auto:border,c_lpad/b_white/f_auto/q_auto/dpr_2.0/c_scale,w_400/ncom/software/switch/70050000007543/6b07a49e1a44becdba659ca76025c33aff3e15863228fc8b0862204cb4d50078",
            "https://assets.nintendo.com/image/upload/ar_16:9,b_auto:border,c_lpad/b_white/f_auto/q_auto/dpr_2.0/c_scale,w_400/ncom/software/switch/70050000007543/9f4e0944f8017ebf9391a1c050dce96ab62632732d52a2c22301eb9c29c57332",
            "https://assets.nintendo.com/image/upload/ar_16:9,b_auto:border,c_lpad/b_white/f_auto/q_auto/dpr_2.0/c_scale,w_400/ncom/software/switch/70050000007543/041eb2b88a234038ea1a1908ab8bce3776dd4f20be94573e7151ab33856ea5dc"
        ]
    },
    {
        "name": "Lethal Company",
        "image": "https://cdn.akamai.steamstatic.com/steam/apps/1966720/capsule_616x353.jpg?t=1700231592",
        "platforms": [
            "PC"
        ],
        "screenshots": [
            "https://cdn.akamai.steamstatic.com/steam/apps/1966720/ss_27eb66c9d0e327f90915cef23b1377e9b10bc27b.1920x1080.jpg?t=1700231592",
            "https://cdn.akamai.steamstatic.com/steam/apps/1966720/ss_08fa3ef83b6eb70313119096f82285fa411f02e5.1920x1080.jpg?t=1700231592",
            "https://cdn.akamai.steamstatic.com/steam/apps/1966720/ss_0499d96a2b9ca0fc8966d77e6d5c95ae94c38492.1920x1080.jpg?t=1700231592",
            "https://assetsio.gnwcdn.com/lethal-company-headline-pajak.jpg?width=1200&height=1200&fit=bounds&quality=70&format=jpg&auto=webp",
            "https://tm.ibxk.com.br/2023/11/20/20090550720011.jpg?ims=1200x675",
            "https://p2.trrsf.com/image/fget/cf/1200/630/middle/images.terra.com/2023/11/20/1118375324-20103132390045.jpg",
            "https://cdn.mos.cms.futurecdn.net/r6a4YjTm9DpgwSA2tVU8qU-320-80.jpg"
        ]
    },
    {
        "name": "Valorant",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Valorant_logo_-_pink_color_version.svg/1200px-Valorant_logo_-_pink_color_version.svg.png",
        "platforms": [
            "PC"
        ],
        "screenshots": [
            "https://i0.wp.com/news.xbox.com/pt-br/wp-content/uploads/sites/8/2023/03/Valorant-56a0b3c0ed6d7752943a.jpg?resize=1920%2C1080&ssl=1",
            "https://cdn2.unrealengine.com/valorant-buy-screen-1920x1080-a9b89319de27.jpg",
            "https://www.m3.se/wp-content/uploads/2023/05/3834054413-63.jpg?quality=50&strip=all",
            "https://i.blogs.es/ca7b3b/valorant/450_1000.webp",
            "https://v.wpimg.pl/ODk5MjguYCUKVztZSA5tMEkPbwMOV2NmHhd3SEhEfXRbTXtdUlo8IkZUKQcOGyY3H0csCQ0UYTMbVikESQUjaxhBIhgGEip2RFMoCxMAPSEPaiIYDhImKgpZYlxXTC5xCQIuXlBBfHdYantfVk12fVkNYwAXEm05",
            "https://www.gamechampions.com/media/d5en15au/valorant-tournaments-on-gamechampions.webp",
            "https://image.hurimg.com/i/hurriyet/75/750x422/65b0d4b6657b1539d2821fbc.jpg"
        ]
    },
    {
        "name": "Cyberpunk 2077",
        "image": "https://image.api.playstation.com/vulcan/ap/rnd/202311/2812/ae84720b553c4ce943e9c342621b60f198beda0dbf533e21.jpg",
        "platforms": [
            "PC",
            "playstation",
            "Xbox"
        ],
        "screenshots": [
            "https://www.dsogaming.com/wp-content/uploads/2020/08/Cyberpunk-2077-new-screenshots-August-2020-1.jpg",
            "https://media.comicbook.com/2020/06/cyberpunk-1-1226316.jpeg?auto=webp&width=1280&height=720&crop=1280:720,smart",
            "https://static.tweaktown.com/news/7/3/73602_07_cyberpunk-2077-looks-amazing-in-these-schmick-new-screenshots_full.jpg",
            "https://www.techpowerup.com/review/cyberpunk-2077-phantom-liberty-benchmark-test-performance-analysis/images/screen001.jpg",
            "https://www.thetechgame.com/images/news/article/2b3e34ef53.jpg",
            "https://assets.rockpapershotgun.com/images/2020/12/Cyberpunk-Photo-Mode-cutscenes-1212x682.jpg",
            "https://cdn.openart.ai/stable_diffusion/5dcfae0bc4d12fdf817dc97cd5a887bdccdc4255_2000x2000.webp"
        ]
    },
    {
        "name": "Minecraft",
        "image": "https://assets.nintendo.com/image/upload/ar_16:9,c_lpad,w_1240/b_white/f_auto/q_auto/ncom/software/switch/70010000000964/811461b8d1cacf1f2da791b478dccfe2a55457780364c3d5a95fbfcdd4c3086f",
        "platforms": [
            "PC",
            "playstation",
            "Xbox"
        ],
        "screenshots": [
            "https://hypixel.net/attachments/2613ee1b-ec24-4977-a729-2c7b878e285f-jpeg.831790/",
            "https://staticg.sportskeeda.com/editor/2022/03/2ee4e-16481582659312-1920.jpg",
            "https://i.imgur.com/LS1wETl.jpeg"
        ]
    },
    {
        "name": "Grand Theft Auto V",
        "image": "https://media.rawg.io/media/games/20a/20aa03a10cda45239fe22d035c0ebe64.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/20a/20aa03a10cda45239fe22d035c0ebe64.jpg",
            "https://media.rawg.io/media/screenshots/a7c/a7c43871a54bed6573a6a429451564ef.jpg",
            "https://media.rawg.io/media/screenshots/cf4/cf4367daf6a1e33684bf19adb02d16d6.jpg",
            "https://media.rawg.io/media/screenshots/f95/f9518b1d99210c0cae21fc09e95b4e31.jpg",
            "https://media.rawg.io/media/screenshots/a5c/a5c95ea539c87d5f538763e16e18fb99.jpg",
            "https://media.rawg.io/media/screenshots/a7e/a7e990bc574f4d34e03b5926361d1ee7.jpg",
            "https://media.rawg.io/media/screenshots/592/592e2501d8734b802b2a34fee2df59fa.jpg"
        ]
    },
    {
        "name": "The Witcher 3: Wild Hunt",
        "image": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Apple Macintosh",
            "Nintendo"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg",
            "https://media.rawg.io/media/screenshots/1ac/1ac19f31974314855ad7be266adeb500.jpg",
            "https://media.rawg.io/media/screenshots/6a0/6a08afca95261a2fe221ea9e01d28762.jpg",
            "https://media.rawg.io/media/screenshots/cdd/cdd31b6b4a687425a87b5ce231ac89d7.jpg",
            "https://media.rawg.io/media/screenshots/862/862397b153221a625922d3bb66337834.jpg",
            "https://media.rawg.io/media/screenshots/166/166787c442a45f52f4f230c33fd7d605.jpg",
            "https://media.rawg.io/media/screenshots/f63/f6373ee614046d81503d63f167181803.jpg"
        ]
    },
    {
        "name": "Portal 2",
        "image": "https://media.rawg.io/media/games/2ba/2bac0e87cf45e5b508f227d281c9252a.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Apple Macintosh",
            "Linux"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/2ba/2bac0e87cf45e5b508f227d281c9252a.jpg",
            "https://media.rawg.io/media/screenshots/221/221a03c11e5ff9f765d62f60d4b4cbf5.jpg",
            "https://media.rawg.io/media/screenshots/173/1737ff43c14f40294011a209b1012875.jpg",
            "https://media.rawg.io/media/screenshots/b11/b11a2ae0664f0e8a1ef2346f99df26e1.jpg",
            "https://media.rawg.io/media/screenshots/9b1/9b107a790909b31918ebe2f40547cc85.jpg",
            "https://media.rawg.io/media/screenshots/d05/d058fc7f7fa6128916c311eb14267fed.jpg",
            "https://media.rawg.io/media/screenshots/415/41543dcc12dffc8e97d85a56ad42cda8.jpg"
        ]
    },
    {
        "name": "Counter-Strike: Global Offensive",
        "image": "https://media.rawg.io/media/games/736/73619bd336c894d6941d926bfd563946.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Linux"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/736/73619bd336c894d6941d926bfd563946.jpg",
            "https://media.rawg.io/media/screenshots/ff1/ff16661bb15f7969b44f6c4118870e44.jpg",
            "https://media.rawg.io/media/screenshots/41b/41bb769d247412eac3336dec934aed72.jpg",
            "https://media.rawg.io/media/screenshots/754/754545acdbf71f56e8902a07c7d20696.jpg",
            "https://media.rawg.io/media/screenshots/fd8/fd873cab4c66db0b8e85d8a66e940074.jpg",
            "https://media.rawg.io/media/screenshots/7db/7db2954f7908b6749c36a5f3c9052f65.jpg",
            "https://media.rawg.io/media/screenshots/337/337a3e98b5933f456a2b37b59fab5f39.jpg"
        ]
    },
    {
        "name": "Tomb Raider (2013)",
        "image": "https://media.rawg.io/media/games/021/021c4e21a1824d2526f925eff6324653.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Apple Macintosh"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/021/021c4e21a1824d2526f925eff6324653.jpg",
            "https://media.rawg.io/media/screenshots/4f9/4f9d5efdecfb63cb99f1baa4c0ceb3bf.jpg",
            "https://media.rawg.io/media/screenshots/80f/80f373082b2a74da3f9c3fe2b877dcd0.jpg",
            "https://media.rawg.io/media/screenshots/a87/a8733e877f8fbe45e4a727c22a06aa2e.jpg",
            "https://media.rawg.io/media/screenshots/3f9/3f91678c6805a76419fa4ea3a045a909.jpg",
            "https://media.rawg.io/media/screenshots/417/4170bf07be43a8d8249193883f87f1c1.jpg",
            "https://media.rawg.io/media/screenshots/2a4/2a4250f83ad9e959d8b4ca9376ae34ea.jpg"
        ]
    },
    {
        "name": "Portal",
        "image": "https://media.rawg.io/media/games/7fa/7fa0b586293c5861ee32490e953a4996.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Android",
            "Apple Macintosh",
            "Linux",
            "Nintendo"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/7fa/7fa0b586293c5861ee32490e953a4996.jpg",
            "https://media.rawg.io/media/screenshots/99e/99e94bd55eb75fa6e75c3dcbb1a570b2.jpg",
            "https://media.rawg.io/media/screenshots/2f0/2f0297a46934d9fa914c626902b1ce20.jpg",
            "https://media.rawg.io/media/screenshots/3b3/3b3713fbca6194dfc4d6e8a8d006d354.jpg",
            "https://media.rawg.io/media/screenshots/c6f/c6f9afc3e4dd51068b22f04acbc6ca99.jpg",
            "https://media.rawg.io/media/screenshots/748/74841207eec76ebc7fc03210168bfb7e.jpg",
            "https://media.rawg.io/media/screenshots/e72/e7256b4caedf099bcb8ebd332f892334.jpg"
        ]
    },
    {
        "name": "Left 4 Dead 2",
        "image": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg",
        "platforms": [
            "PC",
            "Xbox",
            "Apple Macintosh",
            "Linux"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg",
            "https://media.rawg.io/media/screenshots/4c0/4c043fd1a5ff78900483f2e82580fea0.jpg",
            "https://media.rawg.io/media/screenshots/c90/c9071628c238fbc20b366e2413dd8b4a.jpg",
            "https://media.rawg.io/media/screenshots/e29/e293b0f98092b8c0dbe24d66846088bb.jpg",
            "https://media.rawg.io/media/screenshots/168/16867bc76b385eb0fb749e41f7ada93d.jpg",
            "https://media.rawg.io/media/screenshots/fb9/fb917e562f311f48ff8d27632bd29a80.jpg",
            "https://media.rawg.io/media/screenshots/5f2/5f2ca569912add2a211b20ba3f576b97.jpg"
        ]
    },
    {
        "name": "The Elder Scrolls V: Skyrim",
        "image": "https://media.rawg.io/media/games/7cf/7cfc9220b401b7a300e409e539c9afd5.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Nintendo"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/7cf/7cfc9220b401b7a300e409e539c9afd5.jpg",
            "https://media.rawg.io/media/screenshots/3bd/3bd2710bd1ffb6664fdea7b83afd067e.jpg",
            "https://media.rawg.io/media/screenshots/d4e/d4e9b13f54748584ccbd6f998094dade.jpg",
            "https://media.rawg.io/media/screenshots/599/59946a630e9c7871003763d63184404a.jpg",
            "https://media.rawg.io/media/screenshots/c5d/c5dad426038d7d12f933eedbeab48ff3.jpg",
            "https://media.rawg.io/media/screenshots/b32/b326fa01c82db82edd41ed299886ee44.jpg",
            "https://media.rawg.io/media/screenshots/091/091e95b49d5a22de036698fc731395a2.jpg"
        ]
    },
    {
        "name": "Red Dead Redemption 2",
        "image": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg",
            "https://media.rawg.io/media/screenshots/7b8/7b8895a23e8ca0dbd9e1ba24696579d9.jpg",
            "https://media.rawg.io/media/screenshots/b8c/b8cee381079d58b981594ede46a3d6ca.jpg",
            "https://media.rawg.io/media/screenshots/fd6/fd6e41d4c30c098158568aef32dfed35.jpg",
            "https://media.rawg.io/media/screenshots/2ed/2ed3b2791b3bbed6b98bf362694aeb73.jpg",
            "https://media.rawg.io/media/screenshots/857/8573b9f4f06a0c112d6e39cdf3544881.jpg",
            "https://media.rawg.io/media/screenshots/985/985e3e1f1d1af1ab0797d43a95d472cc.jpg"
        ]
    },
    {
        "name": "BioShock Infinite",
        "image": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Linux",
            "Nintendo"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg",
            "https://media.rawg.io/media/screenshots/bf0/bf07e2c6d2c888d372917d9ef453c8a4.jpg",
            "https://media.rawg.io/media/screenshots/9d3/9d38833952812ad7888a6dc21699934f.jpg",
            "https://media.rawg.io/media/screenshots/595/59572d257b6797986e4eabcd1ee023fd.jpg",
            "https://media.rawg.io/media/screenshots/f71/f71c23eb76f050d6180490e82d58d799.jpg",
            "https://media.rawg.io/media/screenshots/871/8713411d5332ceb2b4092073a6f5f3f2.jpg",
            "https://media.rawg.io/media/screenshots/985/985b56daa78e0a23133518d4226e9f97.jpg"
        ]
    },
    {
        "name": "Life is Strange",
        "image": "https://media.rawg.io/media/games/562/562553814dd54e001a541e4ee83a591c.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "iOS",
            "Android",
            "Apple Macintosh",
            "Linux"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/562/562553814dd54e001a541e4ee83a591c.jpg",
            "https://media.rawg.io/media/screenshots/edf/edfcbdf85f02f871263dabf1b4f0aa87.jpg",
            "https://media.rawg.io/media/screenshots/4c6/4c6da2f36396d4ed51f82ba6159fa39b.jpg",
            "https://media.rawg.io/media/screenshots/6aa/6aa56ef1485c8b287a913fa842883daa.jpg",
            "https://media.rawg.io/media/screenshots/cb1/cb148b52fe857f5b0b83ae9c01f56d8e.jpg",
            "https://media.rawg.io/media/screenshots/aea/aea38b33b90054f8fe4cc8bb05253b1d.jpg",
            "https://media.rawg.io/media/screenshots/c1d/c1d6333b2da0f920e8de10c14d3c6093.jpg"
        ]
    },
    {
        "name": "Borderlands 2",
        "image": "https://media.rawg.io/media/games/49c/49c3dfa4ce2f6f140cc4825868e858cb.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Android",
            "Apple Macintosh",
            "Linux"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/49c/49c3dfa4ce2f6f140cc4825868e858cb.jpg",
            "https://media.rawg.io/media/screenshots/adb/adbbb37113618ee107459cd5c344f2a8.jpg",
            "https://media.rawg.io/media/screenshots/616/61643dd96e936d29eb68cf53b2334e53.jpg",
            "https://media.rawg.io/media/screenshots/864/8644946ba14a03ab69f0766c42a03f80.jpg",
            "https://media.rawg.io/media/screenshots/f87/f87ad2b8f02b56e36c57b25cf8eac042.jpg",
            "https://media.rawg.io/media/screenshots/194/194e0962afa272604300001718a07793.jpg",
            "https://media.rawg.io/media/screenshots/297/29716964351ecd82545f1de3a50dfc4e.jpg"
        ]
    },
    {
        "name": "Half-Life 2",
        "image": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg",
        "platforms": [
            "PC",
            "Xbox",
            "Android",
            "Apple Macintosh",
            "Linux"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg",
            "https://media.rawg.io/media/screenshots/8af/8af6188357426890cbc8c8a34d9e7b75.jpg",
            "https://media.rawg.io/media/screenshots/3b5/3b542c954ba5bd2f32da067c8122cd80.jpg",
            "https://media.rawg.io/media/screenshots/3d6/3d6066e45d259d2e83bf6767e6113d94.jpg",
            "https://media.rawg.io/media/screenshots/e49/e49327df2404df6c5dafa8eac7990852.jpg",
            "https://media.rawg.io/media/screenshots/5dd/5dd3e53131bbfe6278bd15b9abe261a0.jpg",
            "https://media.rawg.io/media/screenshots/e99/e995e154d4f9e2df0367adea528a72c5.jpg"
        ]
    },
    {
        "name": "BioShock",
        "image": "https://media.rawg.io/media/games/bc0/bc06a29ceac58652b684deefe7d56099.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Apple Macintosh"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/bc0/bc06a29ceac58652b684deefe7d56099.jpg",
            "https://media.rawg.io/media/screenshots/01f/01f62d7064838a5c3202acfc61503487.jpg",
            "https://media.rawg.io/media/screenshots/7f5/7f517e07e36e4af5a7c0b86a7d42853f.jpg",
            "https://media.rawg.io/media/screenshots/aca/aca089b963a42ec4cbf56b5e5334af8e.jpg",
            "https://media.rawg.io/media/screenshots/3aa/3aa6f71eba1d64e671bd45826ca96560.jpg",
            "https://media.rawg.io/media/screenshots/d8e/d8ed29c7c0b41e4013588847944ed446.jpg",
            "https://media.rawg.io/media/screenshots/146/146e418797aca19296f90d259207414c.jpg"
        ]
    },
    {
        "name": "Destiny 2",
        "image": "https://media.rawg.io/media/games/34b/34b1f1850a1c06fd971bc6ab3ac0ce0e.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Web"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/34b/34b1f1850a1c06fd971bc6ab3ac0ce0e.jpg",
            "https://media.rawg.io/media/screenshots/818/818cc34134cb22fb18fda8edec7144a3.jpg",
            "https://media.rawg.io/media/screenshots/003/003a559bc0b47a4e5f2928f18a8d9142.jpg",
            "https://media.rawg.io/media/screenshots/75d/75d8fbb3254f5b06f1a3f9a026d9c122.jpg",
            "https://media.rawg.io/media/screenshots/ca3/ca3bdc1a51fc90a96c860ab6db8a313c.jpg",
            "https://media.rawg.io/media/screenshots/575/5751a70c954618a99ec574f32be7ad43.jpg",
            "https://media.rawg.io/media/screenshots/2e7/2e7304d3b9e670f943d0bd1e4be090f0.jpg"
        ]
    },
    {
        "name": "God of War (2018)",
        "image": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg",
        "platforms": [
            "PC",
            "PlayStation"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg",
            "https://media.rawg.io/media/screenshots/d68/d6868e5f7bce66e326bd48b11ba24b13.jpeg",
            "https://media.rawg.io/media/screenshots/928/928cdaf4ae204f202d177bbd65e911b3.jpeg",
            "https://media.rawg.io/media/screenshots/a54/a549a06ebe89c570cabb57308c4c42a5.jpeg",
            "https://media.rawg.io/media/screenshots/f02/f0279f8199da3e91134078e737e5fbcf.jpg",
            "https://media.rawg.io/media/screenshots/e87/e87c57660c7c37fe973c6dd6ebcc1ac6.jpeg",
            "https://media.rawg.io/media/screenshots/5b7/5b7280fe437c39d3ce501a867c46a998.jpeg"
        ]
    },
    {
        "name": "Limbo",
        "image": "https://media.rawg.io/media/games/942/9424d6bb763dc38d9378b488603c87fa.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "iOS",
            "Android",
            "Apple Macintosh",
            "Linux",
            "Nintendo"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/942/9424d6bb763dc38d9378b488603c87fa.jpg",
            "https://media.rawg.io/media/screenshots/512/512f4bc2092016478ddcb9e7e60aeec0.jpg",
            "https://media.rawg.io/media/screenshots/63d/63d30699e8fcab9c808e6714d9d3fd59.jpg",
            "https://media.rawg.io/media/screenshots/de0/de04bbc0fd9904071ef25bf23113c8c4.jpg",
            "https://media.rawg.io/media/screenshots/eed/eedbbca4ae2debf2d4e23e55d1f6cff7.jpg",
            "https://media.rawg.io/media/screenshots/59f/59f472b3ed7b414777a29213d70b4d17.jpg",
            "https://media.rawg.io/media/screenshots/e58/e58d31146e4a9e3786dabcbfc30126bc.jpg"
        ]
    },
    {
        "name": "Fallout 4",
        "image": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg",
            "https://media.rawg.io/media/screenshots/f55/f5598897e0e418c67521f2213dceb459.jpg",
            "https://media.rawg.io/media/screenshots/37c/37ce90b25d84e531743917165115d24c.jpg",
            "https://media.rawg.io/media/screenshots/fd3/fd3a97519e6d1b73f429f6bfcfb3bcf5.jpg",
            "https://media.rawg.io/media/screenshots/069/0691b4c1b839e55531d8c3206cd83dd7.jpg",
            "https://media.rawg.io/media/screenshots/cc0/cc0b3e29b579faae8d8585fd9ecff142.jpg",
            "https://media.rawg.io/media/screenshots/99c/99c81029aeace339293753186246099f.jpg"
        ]
    },
    {
        "name": "DOOM (2016)",
        "image": "https://media.rawg.io/media/games/587/587588c64afbff80e6f444eb2e46f9da.jpg",
        "platforms": [
            "PC",
            "PlayStation",
            "Xbox",
            "Nintendo"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/587/587588c64afbff80e6f444eb2e46f9da.jpg",
            "https://media.rawg.io/media/screenshots/353/353c1e834e7da7d6ceaa6beaff529c29.jpg",
            "https://media.rawg.io/media/screenshots/e50/e50f822107b8cc6af57aa21d76524149.jpg",
            "https://media.rawg.io/media/screenshots/ae9/ae9e9f7bfe19c63bd16151f81f81a7ed.jpg",
            "https://media.rawg.io/media/screenshots/14e/14e33eccb109558b0524761340ff2023.jpg",
            "https://media.rawg.io/media/screenshots/45d/45d16955ac9e90141b726684a07db02a.jpg",
            "https://media.rawg.io/media/screenshots/b77/b77629938389a41160d3b2a56eaed568.jpg"
        ]
    },
    {
        "name": "PAYDAY 2",
        "image": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg",
        "platforms": [
            "PC",
            "Xbox",
            "Linux"
        ],
        "screenshots": [
            "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg",
            "https://media.rawg.io/media/screenshots/c38/c38f5aa479eebab20cedcdae370e6e18.jpg",
            "https://media.rawg.io/media/screenshots/442/442be5656b314e3289ecd1486b5282f1.jpg",
            "https://media.rawg.io/media/screenshots/c2c/c2ccfeaeda357f932d1899a91f298850.jpg",
            "https://media.rawg.io/media/screenshots/a18/a18da938def6ce6e5b571f1c20272ab0.jpg",
            "https://media.rawg.io/media/screenshots/a5d/a5da0d01195f01cdedec974d52892128.jpg",
            "https://media.rawg.io/media/screenshots/4ee/4ee5c3c8b850ab4ba8e04b9f5d5ab060.jpg"
        ]
    }
]'''

# Parse the JSON string
games = json.loads(json_string)

for game in games:
    name = game['name']
    image = game['image']
    platforms = game['platforms']
    screenshots = game['screenshots']

    try:
        Game.objects.get(name=name)
        continue
    except:
        gamedb = Game.objects.create(name=name, image=image, platforms=platforms, screenshots=screenshots)
        gamedb.save()

        print(gamedb)