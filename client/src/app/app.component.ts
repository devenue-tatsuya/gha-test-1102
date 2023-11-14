import { Component } from '@angular/core';
import { HeroService } from './hero.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  constructor(private readonly heroService: HeroService) {}

  ngOnInit() {
    // TODO: api疎通確認用。後で削除
    this.heroService.getHeroes().subscribe((res) => {
      console.log('res', res);
    });
  }
}
