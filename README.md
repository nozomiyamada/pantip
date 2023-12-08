# Pantip - Learn, Share & Fun
https://pantip.com/

- each post has one **Post Category** (except for รวมมิตร)
- each post belongs to one **Forum**
- each post may have several tags and comments

## Data 

https://drive.google.com/drive/folders/1DcUoVNpY0V1Kj7MGOuAJFRK9k_IKT1A-

|File Name|Records|File Size|
|:-:|:-:|:-:|
|pantip_random_2013.json|14890|80.9 MB|
|pantip_random_2014.json|14852|74.7 MB|
|pantip_random_2015.json|15926|71.7 MB|
|pantip_random_2016.json|15829|75.2 MB|
|pantip_random_2017.json|19165|78.7 MB|
|pantip_random_2018.json|20143|76.2 MB|
|pantip_random_2019.json|19644|73.1 MB|
|pantip_random_2020.json|17793|69.1 MB|
|pantip_random_2021.json|19303|70.9 MB|
|pantip_random_2022.json|17602|75.9 MB|
|pantip_random_2023.json|19957|72.0 MB|

## Data Dictionary

|Column Name|Data Type|Description|
|:-:|:-:|:-:|
|`url`|string|URL of the post : `"https://pantip.com/topic/<POSTID>"`|
|`time`|string|datetime of the post : `"01/01/2013 18:23:45"`|
|`title`|string|title of the post|
|`post_category`|string|type of the post : {question, general, review, poll, news, sell}|
|`tags`|list|(optional) tags attached to the posts|
|`text`|string|content of the post|
|`profile_name`|string|display name of the author : `"สมาชิกหมายเลข 4534530"`|
|`profile_url`|string|URL of the author profile : `"https://pantip.com/profile/4534530"`|
|`forum`|stirng|forum which the post belongs to|
|`like`|int|the number of likes|
|`emotion_heart`|int|the number of ❤️|
|`emotion_laugh`|int|the number of 😆|
|`emotion_love`|int|the number of 😍|
|`emotion_sad`|int|the number of 🥲|
|`emotion_horror`|int|the number of 😱|
|`emotion_wow`|int|the number of 😳|
|`num_comment`|int|total number of comments|
|`comments`|list|(optional) list of comment dictionary: `{"comment", "like", "priofile_name", "profile_url", "time"}`

## Post Category (6)
1. ถามตอบ (question)
2. พูดคุย (general)
3. รีวิว (review)
4. โพล (poll)
5. ข่าว (news)
6. ซื้อขาย (sell)

## Forums (36)
Description : https://pantip.com/communities/forum

|Forum Name|English|Description|Full URL|
|:-:|:-:|:-:|:-:|
|รวมมิตร|-|รวมกระทู้จากทุกห้อง|https://pantip.com/forum|
|สวนลุมพินี|lumpini|สุขภาพกาย สุขภาพจิต โรคมะเร็ง โรคไมเกรน โรคภูมิแพ้ ปวดประจำเดือน|https://pantip.com/forum/lumpini|
|ราชดำเนิน|rajdumnern|การเมือง รัฐศาสตร์ กฎหมาย สภาผู้แทน รัฐบาล ฝ่ายค้าน พรรคการเมือง|https://pantip.com/forum/rajdumnern|
|สีลม|silom|การบริหารจัดการ การตลาด ทรัพยากรบุคคล งานขาย SME ภาษีนิติบุคคล|https://pantip.com/forum/silom|
|มาบุญครอง|mbk|โทรศัพท์มือถือ Smartphone Tablet iOS Android|https://pantip.com/forum/mbk|
|ไกลบ้าน|klaibann|เรียนต่อต่างประเทศ ทำงานต่างประเทศ วีซ่า|https://pantip.com/forum/klaibann|
|พรหมชาติ|horoscope|ดูดวง ฮวงจุ้ย ไพ่ยิปซี ทำนายฝัน พระเครื่อง|https://pantip.com/forum/horoscope|
|ซิลิคอนวัลเลย์|siliconvalley|คอมมือใหม่ อินเทอร์เน็ต ซอฟต์แวร์ ฮาร์ดแวร์ เกม เขียนโปรแกรม Gadget|https://pantip.com/forum/siliconvalley|
|ดิโอลด์สยาม|theoldsiam|ผู้สูงอายุ สุขภาพผู้สูงอายุ ชีวิตหลังเกษียณ สิทธิผู้สูงอายุ ท่องเที่ยวผู้สูงอายุ|https://pantip.com/forum/theoldsiam|
|ห้องสมุด|library|หนังสือ หนังสือนิยาย ภาษาไทย ภาษาจีน ภาษาอังกฤษ ปรัชญา ประวัติศาสตร์|https://pantip.com/forum/library|
|กล้อง|camera|กล้องถ่ายรูป กล้อง DSLR กล้องวิดีโอ เทคนิคการถ่ายรูป|https://pantip.com/forum/camera|
|จตุจักร|jatujak|สัตว์เลี้ยง สุนัข แมว ต้นไม้ จัดสวน ของสะสม งานฝีมือ เกษตรกรรม|https://pantip.com/forum/jatujak|
|ภูมิภาค|region|ภาคเหนือ ภาคอีสาน ภาคกลาง ภาคตะวันออก ภาคตะวันตก ภาคใต้|https://pantip.com/forum/region|
|แกลเลอรี่|gallery|ภาพถ่ายบุคคล ภาพถ่ายทิวทัศน์ ภาพถ่ายมาโคร|https://pantip.com/forum/gallery|
|กรีนโซน|greenzone|อนุรักษ์สิ่งแวดล้อม อนุรักษ์พลังงาน Green Living การออกแบบเพื่อสิ่งแวดล้อม ผลิตภัณฑ์รักษ์โลก เกษตรอินทรีย์|https://pantip.com/forum/greenzone|
|บางขุนพรหม|tvshow|ละคร นักแสดง ซีรี่ส์ รายการโทรทัศน์ สถานีโทรทัศน์|https://pantip.com/forum/tvshow|
|โต๊ะเครื่องแป้ง|beauty|เครื่องสำอาง เสริมสวย แฟชั่น เครื่องประดับ ลดความอ้วน|https://pantip.com/forum/beauty|
|ชายคา|home|บ้าน คอนโดมิเนียม ตกแต่งบ้าน เฟอร์นิเจอร์ เครื่องใช้ไฟฟ้า เครื่องครัว|https://pantip.com/forum/home|
|ก้นครัว|food|ร้านอาหาร สูตรอาหาร อาหารคาว อาหารหวาน เบเกอรี่ ไอศกรีม|https://pantip.com/forum/food|
|เฉลิมกรุง|chalermkrung|นักร้องนักดนตรี เพลง เครื่องดนตรี คอนเสิร์ต มิวสิควิดีโอ|https://pantip.com/forum/chalermkrung|
|เฉลิมไทย|chalermthai|ภาพยนตร์ ดาราภาพยนตร์ ค่ายหนัง เทศกาลหนัง หนังสั้น|https://pantip.com/forum/chalermthai|
|ชานเรือน|family|ครอบครัว ตั้งครรภ์ ตั้งชื่อลูก การเลี้ยงลูก การสอนลูก|https://pantip.com/forum/family|
|ถนนนักเขียน|writer|แต่งนิยาย เรื่องสั้น กลอน นิทาน|https://pantip.com/forum/writer|
|บลูแพลนเน็ต|blueplanet|เที่ยวไทย เที่ยวต่างประเทศ ทะเล ภูเขา เกาะ น้ำตก ดำน้ำ สายการบิน|https://pantip.com/forum/blueplanet|
|พันทิป|pantip|ข้อเสนอแนะถึงพันทิป วิธีการใช้งานพันทิป กิจกรรมพันทิป|https://pantip.com/forum/pantip|
|รัชดา|ratchada|รถยนต์ มอเตอร์ไซค์ เครื่องเสียงรถยนต์ แต่งรถ การจราจร|https://pantip.com/forum/ratchada|
|ศาลาประชาคม|social|กฎหมาย ปัญหาสังคม ปัญหาชีวิต เศรษฐกิจ คุ้มครองผู้บริโภค|https://pantip.com/forum/social|
|ศาสนา|religious|ศาสนาพุทธ ศาสนาคริสต์ ศาสนาอิสลาม เที่ยววัด ทำบุญ|https://pantip.com/forum/religious|
|ศุภชลาศัย|supachalasai|กีฬา ฟุตบอล บาสเกตบอล มวยสากล กอล์ฟ จักรยาน นักกีฬา|https://pantip.com/forum/supachalasai|
|สยามสแควร์|siam|ชีวิตวัยรุ่น การเรียน โรงเรียน มหาวิทยาลัย ความรักวัยรุ่น เกม|https://pantip.com/forum/siam|
|สินธร|sinthorn|หุ้น เศรษฐกิจ การลงทุน LTF RMF ธนาคาร เงินตราต่างประเทศ|https://pantip.com/forum/sinthorn|
|หว้ากอ|wahkor|วิทยาศาสตร์ วิศวกรรม เทคโนโลยี ฟิสิกส์ ดาราศาสตร์ อวกาศ|https://pantip.com/forum/wahkor|
|หอศิลป์|art|ศิลปะ ภาพวาด ประวัติศาสตร์ศิลป์ สื่อประสม Graphic Design|https://pantip.com/forum/art|
|การ์ตูน|cartoon|การ์ตูนญี่ปุ่น การ์ตูนไทย การ์ตูนฝรั่ง อนิเมะ วาดการ์ตูน ของสะสมจากการ์ตูน คอสเพลย์|https://pantip.com/forum/cartoon|
|บางรัก|bangrak|ความรัก แต่งงาน พรีเวดดิ้ง ปัญหาชีวิตคู่|https://pantip.com/forum/bangrak|
|กรุงโซล|korea|K-POP ซีรีส์เกาหลี นักแสดงเกาหลี อาหารเกาหลี เที่ยวเกาหลี แฟชั่นเกาหลี ภาษาเกาหลี|https://pantip.com/forum/korea|
|แก็ดเจ็ต|gadget|Gadget, Action Camera, Drone, Game Console, Smartwatch, Smartband|https://pantip.com/forum/gadget|
|ไร้สังกัด|isolate|กระทู้อื่นๆ ที่ไม่สังกัดห้องไหนเลย|https://pantip.com/forum/isolate