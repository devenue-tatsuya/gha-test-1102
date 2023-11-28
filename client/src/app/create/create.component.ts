import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

import { HeroService } from '../hero.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss'],
})
export class CreateComponent {
  userCreateForm = new FormGroup({
    userName: new FormControl('', [Validators.required]),
  });

  constructor(private readonly heroService: HeroService) {}

  onSubmit() {
    console.log('onSubmit', this.userCreateForm.getRawValue());
    this.heroService
      .addHero(this.userCreateForm.getRawValue())
      .subscribe((hero: any) => {
        console.log('hero作成完了');
      });
  }
}
