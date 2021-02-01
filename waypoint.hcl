project = "random-sports-team"

app "random-sports-team" {
  
  build {
    use "pack" {}
    registry {
      use "docker" {
        image = "jacobmammoliti/random-sports-team"
        tag   = gitrefpretty()
        local = false
      }
    }
  }

  deploy {
    use "kubernetes" {
      service_port = "8080"
    }
  }

  release {
    use "kubernetes" {
      load_balancer = true
    }
  }
}