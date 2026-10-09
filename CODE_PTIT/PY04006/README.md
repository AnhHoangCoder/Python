Sử dụng lớp Point đã có trong bài 1, khai báo lớp Triangle với thuộc tính là 3 điểm. Viết các phương thức phù hợp để tính diện tích tam giác.

Công thức Heron tính diện tích tam giác khi biết độ dài 3 cạnh là a,b,c:



Input

Dòng đầu ghi số bộ test, không quá 10
Mỗi bộ test ghi trên 1 dòng 6 số thực có giá trị tuyệt đối không quá 1000 lần lượt là tọa độ của 3 điểm. 
Output

Nếu 3 điểm không thể tạo thành tam giác thì in ra INVALID
Nếu 3 điểm tạo thành 1 tam giác thì in ra diện tích của tam giác đó, làm tròn đến 2 chữ số phần thập phân.
Ví dụ


Input

Output

3


0 0 0 5 0 199


1 1 1 1 1 1


0 0 0 5 5 0


	
INVALID


INVALID


12.50