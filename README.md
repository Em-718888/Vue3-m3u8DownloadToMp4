# M3U8 转 MP4 工具

一个纯前端的 M3U8 视频下载转换工具，基于 [FFmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm) 实现，无需后端服务，在浏览器中完成视频合并与格式转换。

## 功能

- 输入 M3U8 地址，在线预览视频（基于 hls.js）
- 自动下载所有 TS 分片并合并
- 使用 FFmpeg.wasm 在浏览器内转换为 MP4 并下载

## 使用方法

### 1. 下载 FFmpeg WASM 核心文件

由于 `ffmpeg-core-0.12.9.wasm` 体积较大（约 31MB），不包含在仓库中，需手动下载后放到项目根目录：

```bash
# 使用 curl
curl -L -o ffmpeg-core-0.12.9.wasm \
  https://unpkg.com/@ffmpeg/core@0.12.9/dist/umd/ffmpeg-core.wasm

# 或使用 wget
wget -O ffmpeg-core-0.12.9.wasm \
  https://unpkg.com/@ffmpeg/core@0.12.9/dist/umd/ffmpeg-core.wasm
```

也可以从 jsDelivr 下载（国内速度更快）：

```
https://cdn.jsdelivr.net/npm/@ffmpeg/core@0.12.9/dist/umd/ffmpeg-core.wasm
```

### 2. 启动本地服务器

FFmpeg.wasm 需要特定的 HTTP 安全头（`Cross-Origin-Embedder-Policy` 等），直接打开 HTML 文件无法使用，必须通过服务器访问。

```bash
python3 server.py
```

启动后访问：`http://localhost:8000/simple.html`

### 3. 使用

1. 在输入框中填入 M3U8 地址
2. 点击「播放视频」可预览
3. 点击「下载MP4格式」开始转换下载
   - 首次使用会加载 FFmpeg WASM（约 30MB），需等待 1-2 分钟
   - 转换完成后自动下载 `video.mp4`

## 项目结构

```
.
├── simple.html              # 主页面
├── server.py                # 本地开发服务器（提供必要的 HTTP 安全头）
├── ffmpeg.js                # FFmpeg.wasm 主库
├── 814.ffmpeg.js            # FFmpeg Worker 文件
├── ffmpeg-core-0.12.9.js    # FFmpeg 核心 JS
└── ffmpeg-core-0.12.9.wasm  # FFmpeg 核心 WASM（需手动下载，见上方说明）
```

## 注意事项

- 需要浏览器支持 `SharedArrayBuffer`，推荐使用 Chrome / Edge 最新版
- M3U8 地址需要支持跨域访问（CORS），否则下载会失败
- 视频较长时内存占用较高，建议在内存充足的设备上使用

## 依赖

- [hls.js](https://github.com/video-dev/hls.js) — M3U8 视频播放
- [FFmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm) v0.12.9 — 浏览器内视频转换
