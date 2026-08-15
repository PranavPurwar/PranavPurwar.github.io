// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.3.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Pranav Purwar",
  title: "Pranav Purwar - CV",
  footer: context { [] },
  top-note: [  ],
  locale-catalog-language: "en",
  text-direction: ltr,
  page-size: "a4",
  page-top-margin: 0.4in,
  page-bottom-margin: 0.4in,
  page-left-margin: 0.45in,
  page-right-margin: 0.45in,
  page-show-footer: true,
  page-show-top-note: true,
  colors-body: rgb(0, 0, 0),
  colors-name: rgb(0, 79, 144),
  colors-headline: rgb(0, 79, 144),
  colors-connections: rgb(0, 79, 144),
  colors-section-titles: rgb(0, 79, 144),
  colors-links: rgb(0, 79, 144),
  colors-footer: rgb(128, 128, 128),
  colors-top-note: rgb(128, 128, 128),
  typography-line-spacing: 0.45em,
  typography-alignment: "justified",
  typography-date-and-location-column-alignment: right,
  typography-font-family-body: "Source Sans 3",
  typography-font-family-name: "Source Sans 3",
  typography-font-family-headline: "Source Sans 3",
  typography-font-family-connections: "Source Sans 3",
  typography-font-family-section-titles: "Source Sans 3",
  typography-font-size-body: 10pt,
  typography-font-size-name: 24pt,
  typography-font-size-headline: 10pt,
  typography-font-size-connections: 10pt,
  typography-font-size-section-titles: 1.25em,
  typography-small-caps-name: false,
  typography-small-caps-headline: false,
  typography-small-caps-connections: false,
  typography-small-caps-section-titles: false,
  typography-bold-name: true,
  typography-bold-headline: false,
  typography-bold-connections: false,
  typography-bold-section-titles: false,
  links-underline: true,
  links-show-external-link-icon: true,
  header-alignment: center,
  header-photo-width: 3.5cm,
  header-space-below-name: 0.25cm,
  header-space-below-headline: 0.25cm,
  header-space-below-connections: 0.25cm,
  header-connections-hyperlink: true,
  header-connections-show-icons: true,
  header-connections-display-urls-instead-of-usernames: false,
  header-connections-separator: "",
  header-connections-space-between-connections: 0.35cm,
  section-titles-type: "with_partial_line",
  section-titles-line-thickness: 0.5pt,
  section-titles-space-above: 0.22cm,
  section-titles-space-below: 0.35cm,
  sections-allow-page-break: true,
  sections-space-between-text-based-entries: 0.15em,
  sections-space-between-regular-entries: 0.35em,
  entries-date-and-location-width: 3.2cm,
  entries-side-space: 0.15cm,
  entries-space-between-columns: 0.1cm,
  entries-allow-page-break: false,
  entries-short-second-row: true,
  entries-degree-width: 1cm,
  entries-summary-space-left: 0cm,
  entries-summary-space-above: 0cm,
  entries-highlights-bullet:  "•" ,
  entries-highlights-nested-bullet:  "•" ,
  entries-highlights-space-left: 0.15cm,
  entries-highlights-space-above: 0cm,
  entries-highlights-space-between-items: 0.1em,
  entries-highlights-space-between-bullet-and-text: 0.4em,
  date: datetime(
    year: 2026,
    month: 8,
    day: 15,
  ),
)


= Pranav Purwar

  #headline([Systems Engineer | JVM Internals & Android Virtualization])

#connections(
  [#connection-with-icon("location-dot")[Delhi, India]],
  [#link("mailto:purwarpranav80@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[purwarpranav80\@gmail.com]]],
  [#link("https://github.com/PranavPurwar", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[PranavPurwar]]],
  [#link("https://linkedin.com/in/pranavpurwar", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[pranavpurwar]]],
)


== Summary

Systems Engineer working on #strong[JVM internals], #strong[compilers], #strong[AI infrastructure], and #strong[Android OS virtualization]. Creator of #strong[Cosmic IDE] (#strong[700+ stars], #strong[100+ forks]), bringing rootless Arch Linux environments to Android, and #strong[Bryte AI Platform] (GraphRAG & FSRS v4 scheduling). Contributor to Android developer tools with #strong[1.2M+ downloads] and #strong[100k+ MAU].

== Experience

#regular-entry(
  [
    #strong[Cosmic IDE | Creator & Architect]

    - #strong[Rootless Linux Environment]: Built a full Arch Linux ARM runtime on Android without root or proot using a custom `glibc` runtime and `LD_PRELOAD` shims to intercept `execve`\/`execvp`\/`posix_spawn`, DNS, and filesystem syscalls.

    - #strong[Recursive Process Sandboxing]: Intercepted process creation chains ensuring child processes (e.g. Gradle daemons, Cargo workers) automatically inherit the shim environment and sandbox boundaries.

    - #strong[Terminal & Package Management]: Built an integrated PTY terminal emulator with process group signal handling (`SIGINT`\/Ctrl+C propagation) and native Arch Linux `pacman` package manager support.

    - #strong[Language & Project Toolchains]: Built a plugin marketplace delivering complete language, project build system (Gradle, Cargo, Maven), and on-device Language Server Protocol (LSP) support across #strong[11+ languages] (Rust, Java, Kotlin, Scala, Go, C\/C++, Python, etc.).

    - #strong[Plugin Architecture]: Engineered dynamic plugin loading for language definitions, custom build commands, and syntax schemas decoupled from core app releases.

  ],
  [
    #link("https://github.com/aload0/Cosmic-IDE")[#strong[GitHub]]

    Aug 2021 – present

  ],
)

#regular-entry(
  [
    #strong[Bryte AI Platform (Open-Source) | Creator & Lead Developer]

    - Built a #strong[Kotlin Multiplatform] backend (Ktor CIO) ingesting PDFs (Mistral OCR), YouTube transcripts (NewPipe extractor), and web pages into structured notes.

    - Implemented #strong[GraphRAG] in Neo4j with #strong[1024-dim vector indexing], weighted Cypher queries balancing document vs cross-document links, automatic semantic chunk interlinking, and Cohere reranking.

    - Wrote a native Kotlin port of #strong[FSRS v4] (spaced repetition algorithm) to compute card stability, difficulty, and retrievability without external dependencies.

    - Orchestrated multi-step LLM workflows using JetBrains Koog with context compression, plus a streaming Markdown parser with mid-stream table recovery.

    - Streamed generated flashcards and questions in real time using type-safe #strong[`kotlinx.rpc` over WebSockets], multiplexing multiple services over a single connection.

  ],
  [
    #link("https://github.com/Bryte-Edu/server")[#strong[GitHub]]

    Sept 2024 – present

  ],
)

#regular-entry(
  [
    #strong[OpenJDK & Kotlin Compiler Ports (Android)]

    - #strong[Compiler Ports]: Ported `javac` (OpenJDK 27 EA, Java 26 support) and `kotlinc` (Kotlin 2.4\/2.5) to run directly on Android Runtime (#strong[ART]); published artifacts to JitPack.

    - #strong[NIO & Memory Fixes]: Bypassed Android's restricted NIO via custom `ZipFileSystem` for `ct.sym`; used HiddenApi Bypass to invoke `NioUtils.freeDirectBuffer`, fixing fatal off-heap OOM crashes during JAR parsing.

    - #strong[Upstream Contribution]: Authored PR #link("https://github.com/JetBrains/kotlin/pull/5146")[`JetBrains/kotlin#5146`] fixing a direct-buffer memory leak in `ZipImplementation` when using `-Xuse-fast-jar-file-system`.

  ],
  [
    #link("https://github.com/PranavPurwar/javac-android")[#strong[OpenJDK]] | #link("https://github.com/PranavPurwar/kotlinc-android")[#strong[Kotlin]]

    Sept 2023 – present

  ],
)

#regular-entry(
  [
    #strong[Sketchware-Pro | Core Team]

    - Core team member for Android IDE (#strong[1.7k+ stars], #strong[670+ forks], #strong[100k+ MAU]) integrating ported Kotlin\/Java compilers.

    - Integrated #strong[R8\/D8 Code Shrinker] and added Java 9\/11+ compilation pipelines, cutting output APK sizes by #strong[\~40\%].

    - Engineered on-device compile-time #strong[ViewBinding generator] from XML layouts and recursive AAR\/JAR dependency resolver.

  ],
  [
    #link("https://github.com/Sketchware-Pro/Sketchware-Pro")[#strong[GitHub]]

    Aug 2021 – present

  ],
)

#regular-entry(
  [
    #strong[Reef | Creator]

    - Built an open-source Android screen time & productivity app (#strong[320+ stars], on IzzyOnDroid) with #strong[Jetpack Compose] and Material 3 Expressive.

    - Normalized inconsistent `UsageStatsManager` events across fragmented OEM ROMs (MIUI, OneUI) to accurately calculate per-app screen time.

    - Implemented real-time app and website blocking, Pomodoro focus timers, and routines using `AccessibilityService` and `NotificationListenerService`.

  ],
  [
    #link("https://github.com/aload0/Reef")[#strong[GitHub]]

    Sept 2024 – present

  ],
)

== Skills

#strong[Languages:] Kotlin, Java, Python, TypeScript, C, JVM Bytecode, DEX\/ART

#strong[Compiler & Systems:] OpenJDK, kotlinc, ART Runtime, LSP, Gradle, R8\/D8, glibc, LD\_PRELOAD, Linux Virtualization, ELF\/PTY, HiddenApi Bypass

#strong[Backend & AI Infrastructure:] Ktor, Neo4j, GraphRAG, Cypher, FSRS v4, LLM Agents (Koog), kotlinx.rpc, WebSockets, Mistral AI, Cohere, SSE Streaming

#strong[Mobile & Platforms:] Android SDK, Jetpack Compose, Kotlin Multiplatform (KMP), Material 3 Expressive, IzzyOnDroid \/ F-Droid
