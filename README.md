# PatchWorks
Python Pipeline Data Processing Sample

## 作成計画

OpenCVを使って生成したカメラデータ、またはMP4ファイルをパイプライン構造で各処理単位に渡し、データ解析を行う構造（テンプレート）を作る。

* FactoryMethodで各プロダクト(処理単位）をエレメント（dequeue）で連結する。
* PC間を跨ぐことを想定し、TCP/UDPとLZ4で通信連携できるようにする。
* VideoCaptureProduct、VideoPlayProduct、DataFilingElement、TcpSendElement、TcpReceiveElement、UdpSendElement、UdpReceiveElement、DataStoreElement(SqLite3)などが基本エレメント。
* 連結エレメントはObserverの仕組みでｎ対ｎ接続が可能。
* FactoryMethodは、iniファイルかjsonファイルからエレメント、プロダクトを生成し、連結情報から動的に構成できるようにする。
* 途中からdequeueをRingBufferに変更して、メモリ生成・消滅の回数を減らして速度アップを確認する。
* バイナリデータ(cv::Mat)と同時にフレーム番号、フレーム時刻なども保存する。
* VideoViewProductでプレビューするときは、リアルタイム～5FPSまで可変できるようにする。
* OpenCVのAI機能で顔や人物の矩形判定を画像データと一緒に載せてファイル保存する。これの再生機能も。

隣のAlternateプロジェクト(C/C++)でやっている事をPythonで作ったらどんな感じか？というのを確認できるようにするところまで、コツコツとやってみましょう。

## 現在の構成

現在までに出来上がっている構成は以下のイメージです。

```
ClockElement → QueueElement → QueueElement → TerminateElement
               └VideoCapture  └VideoView
```
