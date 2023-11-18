# 阶段1：构建
FROM node:14 AS build-stage

# 设置工作目录
WORKDIR /app

# 复制package.json和package-lock.json
COPY package*.json ./

# 安装项目依赖
RUN npm install

# 复制项目文件和文件夹到工作目录
COPY . .

# 构建应用
RUN npm run build

# 阶段2：运行时
FROM nginx:stable-alpine as production-stage

# 将构建出的文件从构建阶段复制到当前镜像
COPY --from=build-stage /app/dist /usr/share/nginx/html

# 暴露80端口
EXPOSE 80

# 运行nginx
CMD ["nginx", "-g", "daemon off;"]
