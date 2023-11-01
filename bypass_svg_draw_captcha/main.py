from requests import session # rquests để lấy giá trị svg qua api
from urllib3 import disable_warnings , exceptions # tắt đi cảnh báo khi requests với tùy chọn verfy = False , trust = False
from re import findall # regex để tìm tất cả giá trị d
from cairosvg import svg2png
from pytesseract import image_to_data
from cv2 import imread , cvtColor , imread , resize , INTER_LINEAR , medianBlur , imwrite , COLOR_BGR2RGB
disable_warnings(exceptions.InsecureRequestWarning)

ss = session()
def get_svg_captcha():
    """
    test trên web này nhé ae => hoadondientu.gdt.gov.vn
    api captcha
    """
    ss = session()
    ss.trust_env = ss.verify = False
    response = ss.get('https://hoadondientu.gdt.gov.vn:30000/captcha')
    svg_content = response.json()['content']
    return svg_content

def svg_remix(svg_content,svg_path):
    
    """ cấu trúc của một chữ để tạo thành svg sẽ như này => <svg xmlns="http://www.w3.org/2000/svg" width="200" height="40" viewBox="0,0,200,40"></svg>"""
    """cấu trúc của một chữ trong svg sẽ như này => <path fill="#333" d="[d sẽ truyền vào đây]"/> """
    
    prefix = '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="40" viewBox="0,0,200,40">'
    suffix =  '</svg>'
    d_values = findall(r'd="(.*?)"/>',svg_content)
    list_d_svg = []
    for d in d_values:
        #  lưu từng giá trị d ra file cho các bác thấy rõ
        with open(str(d_values.index(d)) + '.txt','w',encoding='utf-8') as f:
            f.write(d)
        if 'fill="none' not in d:
            list_d_svg.append(f'<path fill="#333" d="{d}"/>')
            
    
    d_svg = ''.join(list_d_svg)
    svg_full = prefix + d_svg + suffix
    with open(svg_path,'w' , encoding='utf-8') as f:
        f.write(svg_full)
    
def svg_png(svg_path,png_path):
    svg2png(url=svg_path , write_to=png_path)
    
    
        
def image_to_text(img_path):
    # #  đổi kích thước ảnh
    # img_content = imread(img_path)
    # img_resize = resize(img_content, None, fx=15, fy=15, interpolation=INTER_LINEAR)
    # img = medianBlur(img_resize, 5)
    # imwrite(img_path,img)
    
    # #  đọc lại ảnh
    img_content = imread(img_path)
    # img_convert = cvtColor(img_content,COLOR_BGR2RGB)
    boxes = image_to_data(img_content)
    print(boxes)
    print()
    text = ''
    for x , b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                text = (b[-1])
                print(text)
        
                
    
if __name__ == '__main__':
    svg_content = get_svg_captcha()
    svg_path = 'test.svg'
    svg_remix(svg_content,svg_path)
    svg2png_path = 'test_svg.png'
    # chuyển svg sang ảnh png
    svg2png(url=svg_path,write_to=svg2png_path)
    
    # chuyển ảnh sang text
    # image_to_text(svg2png_path)
    