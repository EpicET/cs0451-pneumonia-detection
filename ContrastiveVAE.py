import torch
import torch.nn as nn

#variational autoencoder w contrastive learning :)
class ContrastiveVAE(nn.Module):
    def __init__(self, latent_dim=64):
        super(ContrastiveVAE, self).__init__()
        self.latent_dim = latent_dim

        # Encoder CNN
        self.encoder_cnn = nn.Sequential(
            nn.Conv2d(1, 32, 4, 2, 1),  # (B, 32, 112, 112)
            nn.ReLU(),
            nn.Conv2d(32, 64, 4, 2, 1), # (B, 64, 56, 56)
            nn.ReLU(),
        )

        self.flattened_size = 64 * 56 * 56
        self.encoder_flatten = nn.Flatten()
        self.fc_mu = nn.Linear(self.flattened_size, latent_dim)
        self.fc_logvar = nn.Linear(self.flattened_size, latent_dim)

        # Decoder (not really using had from before)
        self.decoder_input = nn.Linear(latent_dim, self.flattened_size)
        self.decoder = nn.Sequential(
            nn.Unflatten(1, (64, 56, 56)),
            nn.ConvTranspose2d(64, 32, 4, 2, 1),  # (B, 32, 112, 112)
            nn.ReLU(),
            nn.ConvTranspose2d(32, 1, 4, 2, 1),   # (B, 1, 224, 224)
            nn.Sigmoid()
        )

    def encode(self, x):
        x = self.encoder_cnn(x)
        x = self.encoder_flatten(x)
        mu = self.fc_mu(x)
        logvar = self.fc_logvar(x)
        return mu, logvar

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z):
        x = self.decoder_input(z)
        x = self.decoder(x)
        return x

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        x_recon = self.decode(z)
        return x_recon, mu, logvar
    
    def supervised_contrastive_loss(embeddings, labels, temperature=0.1):
    #contrastive loss function for VAE

        device = embeddings.device
        labels = labels.contiguous().view(-1, 1)
        mask = torch.eq(labels, labels.T).float().to(device)

        dot_product = (embeddings @ embeddings.T) / temperature
        logits_max, _ = torch.max(dot_product, dim=1, keepdim=True)
        logits = dot_product - logits_max.detach()

        exp_logits = torch.exp(logits) * (1 - torch.eye(len(labels), device=device))
        log_prob = logits - torch.log(exp_logits.sum(1, keepdim=True) + 1e-8)

        mean_log_prob_pos = (mask * log_prob).sum(1) / mask.sum(1)
        loss = -mean_log_prob_pos.mean()
        return loss


