disabled = 'Tắt'
enabled = 'Bật'
subtle_variation = 'Biến đổi nhẹ'
strong_variation = 'Biến đổi mạnh'
upscale_15 = 'Phóng lớn (1.5x)'
upscale_2 = 'Phóng lớn (2x)'
upscale_fast = 'Phóng lớn (Nhanh 2x)'

uov_list = [
    disabled, subtle_variation, strong_variation, upscale_15, upscale_2, upscale_fast
]

KSAMPLER_NAMES = ["euler", "euler_ancestral", "heun", "heunpp2","dpm_2", "dpm_2_ancestral",
                  "lms", "dpm_fast", "dpm_adaptive", "dpmpp_2s_ancestral", "dpmpp_sde", "dpmpp_sde_gpu",
                  "dpmpp_2m", "dpmpp_2m_sde", "dpmpp_2m_sde_gpu", "dpmpp_3m_sde", "dpmpp_3m_sde_gpu", "ddpm", "lcm"]

SCHEDULER_NAMES = ["bình thường", "karras", "mũi tên số", "đồng đều sgm", "đơn giản", "ddim đồng đều", "lcm", "turbo"]
SAMPLER_NAMES = KSAMPLER_NAMES + ["ddim", "uni_pc", "uni_pc_bh2"]

sampler_list = SAMPLER_NAMES
scheduler_list = SCHEDULER_NAMES

cn_ip = "Hình ảnh gợi ý"
cn_ip_face = "Đổi khuôn mặt"
cn_canny = "PyraCanny"
cn_cpds = "CPDS"

ip_list = [cn_ip, cn_canny, cn_cpds, cn_ip_face]
default_ip = cn_ip

default_parameters = {
    cn_ip: (0.5, 0.6), cn_ip_face: (0.9, 0.75), cn_canny: (0.5, 1.0), cn_cpds: (0.5, 1.0)
}  # dừng, trọng số

inpaint_engine_versions = ['Không có', 'v1', 'v2.5', 'v2.6']
performance_selections = ['Tốc độ', 'Chất lượng', 'Tốc độ cực kỳ']
performance_selections1 = ['Speed', 'Quality', 'Extreme Speed']

inpaint_option_default = 'Vẽ lại hoặc Xoá bỏ (mặc định)'
inpaint_option_detail = 'Cải thiện chi tiết (khuôn mặt, tay, mắt, v.v.)'
inpaint_option_modify = 'Chỉnh sửa Nội dung (thêm đối tượng, thay đổi nền, v.v.)'
inpaint_options = [inpaint_option_default, inpaint_option_detail, inpaint_option_modify]

desc_type_photo = 'Ảnh chụp'
desc_type_anime = 'Nghệ thuật/Anime'
