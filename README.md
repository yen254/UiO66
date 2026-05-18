# Nghiên cứu Xúc tác Cu-Ni/MIL-101 và UiO-66

Dự án này tập trung nghiên cứu vật liệu xúc tác Cu-Ni mang trên chất nền khung kim loại - hữu cơ (MOF) là MIL-101 và UiO-66. Mục tiêu chính là ứng dụng các vật liệu này cho phản ứng chuyển hóa trực tiếp khí carbon dioxide (CO₂) và methanol thành dimethyl carbonate (DMC).

## Tổng quan Dự án

Phản ứng tổng hợp trực tiếp DMC từ CO₂ và methanol đang thu hút nhiều sự quan tâm vì nó không chỉ giúp tận dụng CO₂ (giảm hiệu ứng nhà kính) mà còn thay thế các quy trình sản xuất DMC truyền thống độc hại (sử dụng phosgene). Tuy nhiên, phản ứng này bị giới hạn bởi mặt nhiệt động học. Việc phát triển các hệ xúc tác hiệu quả, như Cu-Ni/UiO-66, là chìa khóa để giải quyết vấn đề này.

### Các thành phần chính của dự án:
1. **Tổng hợp vật liệu**: Quy trình chế tạo MIL-101 và UiO-66, sau đó mang các kim loại hoạt tính Cu và Ni lên chất mang.
2. **Đặc trưng hóa lý**: Sử dụng các phương pháp như XRD, SEM-EDS, v.v., để đánh giá cấu trúc và hình thái của xúc tác.
3. **Mô phỏng phân tử**: Sử dụng Python (thư viện ASE) để mô phỏng định tính quá trình hấp phụ và kích hoạt CO₂ trên tâm axit Lewis (Zr) của UiO-66, hỗ trợ cho việc giải thích cơ chế phản ứng.

## Cấu trúc Thư mục

- `docs/`: Chứa các tài liệu chi tiết về dự án (tổng quan cơ chế, mô phỏng).
- `generate_figures.py`: Kịch bản Python dùng để mô phỏng và xuất hình ảnh cấu trúc phân tử (CO₂, Methanol, DMC, và mô hình tâm Zr).
- `venv/`: Môi trường ảo Python (để chạy script mô phỏng).

## Hướng dẫn Chạy Dự án (Sử dụng `uv`)

Dự án này sử dụng công cụ `uv` để quản lý môi trường và chạy các kịch bản Python một cách nhanh chóng và cô lập.

### 1. Chạy mã thử nghiệm chính
Bạn có thể kiểm tra dự án bằng lệnh:
```bash
uv run main.py
```

### 2. Mô phỏng Phân tử
Script `generate_figures.py` đã được nhúng sẵn các siêu dữ liệu cấu hình thư viện. Để chạy kịch bản sinh hình ảnh mô phỏng phân tử (publication-quality), hãy sử dụng lệnh:
```bash
uv run generate_figures.py
```

Các hình ảnh xuất ra sẽ được dùng để hỗ trợ trực tiếp cho phần bàn luận cơ chế trong báo cáo hoặc bài báo khoa học.

## Tác giả
- Nguyễn Thị Hà An (Đồ án Tốt nghiệp - Kỹ thuật Hóa học, Đại học Bách khoa Hà Nội)
