---
name: boss-zhipin
description: >
  Search Boss直聘 (BOSS Zhipin), 拉勾 (Lagou), and 猎聘 (Liepin) for performance marketing,
  digital marketing, paid media, and related roles in China. Optimized for the Chinese job market
  including salary in RMB, major cities (Shanghai, Beijing, Shenzhen, Guangzhou, Hangzhou, Chengdu),
  and Chinese hiring patterns. Use when the user wants to find marketing jobs in China.
---

# Boss直聘 & China Job Boards — Specialist

## Search Strategy

### Platform URLs
- **Boss直聘**: `https://www.zhipin.com/`
- **拉勾**: `https://www.lagou.com/`
- **猎聘**: `https://www.liepin.com/`

### Chinese Job Market Context

**Major Marketing Hubs:**
- **Shanghai** — Largest market, MNC regional HQs, agencies, e-commerce
- **Beijing** — Tech giants (Baidu, ByteDance), government, media
- **Shenzhen** — Tencent, hardware companies, cross-border e-commerce
- **Guangzhou** — Trade, manufacturing, e-commerce
- **Hangzhou** — Alibaba ecosystem, e-commerce
- **Chengdu** — Growing tech scene, gaming

**Market Specifics:**
- Salary quoted monthly, before tax (税前)
- Social insurance + housing fund (五险一金) deducted from salary
- 996 culture in some companies (9am-9pm, 6 days) — ask about work hours
- Chinese platforms dominate: WeChat Ads, Douyin (TikTok China), Baidu Ads, Xiaohongshu
- International platforms (Google, Meta) used mainly for cross-border/overseas marketing
- "五险一金" (social insurance + housing fund) is standard benefit

### Key Chinese Marketing Platforms
- **百度推广** (Baidu Ads) — Search marketing
- **腾讯广告/微信广告** (Tencent/WeChat Ads) — Social advertising
- **巨量引擎/抖音** (Ocean Engine/Douyin) — Short video advertising
- **小红书** (Xiaohongshu/RED) — Lifestyle/social commerce
- **阿里妈妈** (Alimama) — E-commerce advertising (Taobao/Tmall)
- **京东京准通** (JD Jingtong) — JD.com advertising

### Salary Benchmarks (RMB, Monthly, Pre-tax)
| Role | Junior | Mid | Senior | Manager |
|---|---|---|---|---|
| Performance Marketing | 8-15K | 15-25K | 25-40K | 40-70K |
| Paid Media | 7-12K | 12-20K | 20-35K | 35-60K |
| Growth Marketing | 10-18K | 18-30K | 30-50K | 50-90K |

### Search Method
1. Use `mimo_web_search` with Chinese keywords: "效果营销 招聘 {城市}"
2. Also search: "数字营销 招聘", "付费投放 招聘", "SEM 招聘"
3. Use `web_fetch` where accessible (some sites block scrapers)

### Chinese Keyword Map
```
Performance Marketing = 效果营销 / 绩效营销
Paid Media = 付费投放 / 付费媒体
PPC/SEM = 搜索引擎营销 / SEM
Paid Social = 社交广告投放
Growth Marketing = 增长营销
Google Ads = 谷歌广告 (mainly for cross-border)
Meta Ads = Meta广告 / Facebook广告 (mainly for cross-border)
WeChat Ads = 微信广告 / 腾讯广告
Douyin Ads = 抖音广告 / 巨量引擎
```

## Output

```
## 💼 中国招聘: [Role] in [Location]

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [City] | 💰 [月薪 税前] | 🕐 [Posted]
- 🏢 [公司类型: 外企/民企/创业公司/Agency]
- ⏰ [工作时间: 是否996]
- 🔗 [Link]
- **Key Requirements**: [summary]
```

## Rules

- Always show salary in RMB, monthly, pre-tax
- Note if the role is for domestic or cross-border/overseas marketing
- Flag work hours (996 warning if relevant)
- Chinese platforms (Douyin, WeChat, Xiaohongshu) are the primary channels for domestic roles
