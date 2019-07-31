(ns basic-app.workspaces
  (:require
    [nubank.workspaces.core :as ws]
    [basic-app.demo-ws]))

(defonce init (ws/mount))
