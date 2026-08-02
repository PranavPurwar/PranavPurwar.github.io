# Pranav Purwar's CV

- Email: [purwarpranav80@gmail.com](mailto:purwarpranav80@gmail.com)
- Location: Delhi, India
# Pranav Purwar — Systems Engineer

- Email: [purwarpranav80@gmail.com](mailto:purwarpranav80@gmail.com)
- Location: Delhi, India
- GitHub: [PranavPurwar](https://github.com/PranavPurwar)
- LinkedIn: [pranavpurwar](https://linkedin.com/in/pranavpurwar)

## Summary
Systems engineer focused on JVM internals, compiler toolchains, AI infrastructure, and Android OS-level virtualization. Creator and maintainer of production open-source platforms (Cosmic IDE, Bryte AI) used by large developer communities; proven track record shipping cross-platform backends, compiler ports, and systems-level tooling.

## Selected Experience

### Bryte AI Platform — Creator & Lead Developer (Sept 2024 – Present)
[GitHub](https://github.com/Bryte-Edu/server)
- Designed a Kotlin Multiplatform backend for multi-modal ingestion (PDF/OCR, YouTube, web), enabling robust document reconstruction and retrieval.
- Implemented production GraphRAG with a 1024-dim vector index, weighted Cypher retrieval, and automatic semantic chunk interlinking (thresholds ≥0.65).
- Ported FSRS v4 to Kotlin (native) and built stateful agent orchestration supporting 100k+ token windows and real-time streaming clients.

### Cosmic IDE — Creator & Architect (Aug 2021 – Present)
[GitHub](https://github.com/Cosmic-IDE/Cosmic-IDE)
- Built a full Linux environment on Android without root using a custom glibc runtime and LD_PRELOAD shims to virtualize filesystem, DNS, and process execution.
- Engineered recursive process sandboxing and a native PTY with correct signal/foreground handling for interactive shells.
- Built a plugin marketplace and 11 language integrations; project has 686+ stars and extensive community adoption.

### OpenJDK & Kotlin Compiler Ports (Android) — Lead Systems Developer (Sept 2023 – Present)
[javac-android](https://github.com/PranavPurwar/javac-android) · [kotlinc-android](https://github.com/PranavPurwar/kotlinc-android)
- Ported javac (OpenJDK 27 EA) and kotlinc (2.4+) to ART, maintaining patches and syncing with upstream.
- Reworked platform resolution and implemented a custom ZipFileSystem for ct.sym to bypass Android NIO limitations.
- Added memory-reclamation hooks (HiddenApiBypass) to prevent OOMs during large JAR parsing.

### Sketchware‑Pro — Core Team & Technical Lead (Aug 2021 – Present)
[GitHub](https://github.com/Sketchware-Pro/Sketchware-Pro)
- Core contributor to a mobile IDE with 1.6k+ stars and ~100k MAU; designed build pipelines and integrated R8 to reduce APK sizes ≈40%.

### Reef — Systems Architect (Sept 2024 – Present)
[GitHub](https://github.com/aload0/Reef)
- Architected Android-level telemetry and OEM-normalization (UsageCalculator), and implemented robust notification routing under strict background execution policies.

## Selected Projects & Contributions
- Cosmic IDE — OS virtualization on Android (LD_PRELOAD shims, sandboxing, PTY)
- Bryte AI — GraphRAG, native FSRS v4 port, large-context agents
- JetBrains/kotlin — upstream PR fixing a critical memory leak (PR #5146)

## Impact
- Open-source reach: 1.2M+ downloads across projects; 30k+ daily users in related ecosystems.
- Notable repo: Cosmic IDE (686+ stars, 100+ forks).

## Technical Skills
- Languages: Kotlin, Java, C/C++, Python, TypeScript
- Systems: glibc internals, dynamic linking, LD_PRELOAD, PTY, ELF
- Compilers & Tooling: OpenJDK, kotlinc, ART, LSP, Gradle, R8/D8
- Backend & AI: Ktor, Neo4j (GraphRAG), vector search, FSRS v4, SSE/WebSockets
- Mobile & Platforms: Android SDK, Jetpack Compose, Kotlin Multiplatform

## Publications & Links
- GitHub: https://github.com/PranavPurwar
- Selected PR: https://github.com/JetBrains/kotlin/pull/5146

---

If you'd like, I can:
- produce a one-page printable PDF with improved layout (print CSS), or
- convert this into a compact one-page HTML/CSS resume for downloads.
